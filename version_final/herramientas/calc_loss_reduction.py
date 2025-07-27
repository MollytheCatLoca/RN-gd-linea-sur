#!/usr/bin/env python3
"""
calc_loss_reduction.py
Herramienta para calcular reducción de pérdidas con generación distribuida
Aplicable a toda la Línea Sur con múltiples puntos de inyección
"""

import numpy as np
from typing import Dict, List, Tuple
import pandas as pd

class LossReductionCalculator:
    """Calculadora para reducción de pérdidas técnicas con GD"""
    
    def __init__(self, network_config: Dict):
        """
        Inicializa calculadora con configuración de red
        
        Args:
            network_config: Diccionario con parámetros de red
                - stations: Lista de estaciones con distancias
                - conductor_data: Datos de conductores por tramo
                - base_mva: Potencia base
                - voltage_kv: Voltaje nominal
        """
        self.stations = network_config['stations']
        self.conductor_data = network_config['conductor_data']
        self.base_mva = network_config['base_mva']
        self.voltage_kv = network_config['voltage_kv']
        
        # Calcular impedancias base
        self.z_base = self.voltage_kv**2 / self.base_mva
        
    def calculate_line_losses(self, power_flow: List[Dict]) -> Dict:
        """
        Calcula pérdidas I²R en cada tramo de línea
        
        Args:
            power_flow: Lista de flujos por tramo [{from, to, p_mw, q_mvar}]
            
        Returns:
            Diccionario con pérdidas por tramo y totales
        """
        total_losses = 0
        losses_by_section = []
        
        for flow in power_flow:
            # Obtener datos del conductor
            section_key = f"{flow['from']}_{flow['to']}"
            if section_key not in self.conductor_data:
                continue
                
            conductor = self.conductor_data[section_key]
            r_ohm = conductor['r_ohm_per_km'] * conductor['length_km']
            
            # Calcular corriente
            s_mva = np.sqrt(flow['p_mw']**2 + flow['q_mvar']**2)
            i_ka = s_mva / (np.sqrt(3) * self.voltage_kv)
            
            # Pérdidas I²R
            losses_mw = 3 * i_ka**2 * r_ohm / 1000
            
            losses_by_section.append({
                'section': section_key,
                'current_ka': i_ka,
                'losses_mw': losses_mw,
                'losses_percent': (losses_mw / flow['p_mw'] * 100) if flow['p_mw'] > 0 else 0
            })
            
            total_losses += losses_mw
        
        return {
            'total_losses_mw': total_losses,
            'losses_by_section': losses_by_section,
            'total_losses_percent': (total_losses / power_flow[0]['p_mw'] * 100) if power_flow[0]['p_mw'] > 0 else 0
        }
    
    def simulate_gd_injection(self, gd_locations: List[Dict], load_profile: Dict) -> Dict:
        """
        Simula inyección de GD y calcula nuevas pérdidas
        
        Args:
            gd_locations: Lista de GD [{station, p_mw, location_km}]
            load_profile: Perfil de carga por estación
            
        Returns:
            Diccionario con análisis comparativo
        """
        # Caso base sin GD
        base_flow = self._calculate_power_flow(load_profile, [])
        base_losses = self.calculate_line_losses(base_flow)
        
        # Caso con GD
        gd_flow = self._calculate_power_flow(load_profile, gd_locations)
        gd_losses = self.calculate_line_losses(gd_flow)
        
        # Reducción de pérdidas
        loss_reduction_mw = base_losses['total_losses_mw'] - gd_losses['total_losses_mw']
        loss_reduction_percent = (loss_reduction_mw / base_losses['total_losses_mw'] * 100) if base_losses['total_losses_mw'] > 0 else 0
        
        # Análisis por ubicación GD
        gd_impact = []
        for gd in gd_locations:
            # Calcular impacto individual (aproximado)
            local_reduction = self._estimate_local_impact(gd, base_flow)
            gd_impact.append({
                'location': gd['station'],
                'gd_mw': gd['p_mw'],
                'local_loss_reduction_mw': local_reduction,
                'efficiency': local_reduction / gd['p_mw'] if gd['p_mw'] > 0 else 0
            })
        
        return {
            'base_case': {
                'total_losses_mw': base_losses['total_losses_mw'],
                'losses_percent': base_losses['total_losses_percent']
            },
            'gd_case': {
                'total_losses_mw': gd_losses['total_losses_mw'],
                'losses_percent': gd_losses['total_losses_percent']
            },
            'reduction': {
                'loss_reduction_mw': loss_reduction_mw,
                'loss_reduction_percent': loss_reduction_percent,
                'annual_energy_saved_mwh': loss_reduction_mw * 8760,
                'annual_value_usd': loss_reduction_mw * 8760 * 122.7
            },
            'gd_impact': gd_impact
        }
    
    def _calculate_power_flow(self, loads: Dict, gd_list: List[Dict]) -> List[Dict]:
        """
        Calcula flujo de potencia simplificado (DC power flow)
        
        Args:
            loads: Cargas por estación
            gd_list: Lista de generadores distribuidos
            
        Returns:
            Lista de flujos por tramo
        """
        # Crear diccionario de inyecciones netas
        net_injection = {}
        
        # Añadir cargas (negativas)
        for station, load in loads.items():
            net_injection[station] = -load['p_mw']
        
        # Añadir generación (positiva)
        for gd in gd_list:
            if gd['station'] in net_injection:
                net_injection[gd['station']] += gd['p_mw']
            else:
                net_injection[gd['station']] = gd['p_mw']
        
        # Calcular flujos desde el final hacia Pilcaniyeu
        flows = []
        accumulated_flow = 0
        
        # Ordenar estaciones por distancia (de mayor a menor)
        sorted_stations = sorted(self.stations, key=lambda x: x['distance_km'], reverse=True)
        
        for i in range(len(sorted_stations) - 1):
            current = sorted_stations[i]
            next_upstream = sorted_stations[i + 1]
            
            # Añadir inyección local al flujo acumulado
            if current['name'] in net_injection:
                accumulated_flow += net_injection[current['name']]
            
            # Flujo en el tramo
            flows.append({
                'from': next_upstream['name'],
                'to': current['name'],
                'p_mw': accumulated_flow,
                'q_mvar': accumulated_flow * 0.3  # Asumiendo tan(φ) = 0.3
            })
        
        return flows
    
    def _estimate_local_impact(self, gd: Dict, base_flow: List[Dict]) -> float:
        """
        Estima impacto local de un GD en reducción de pérdidas
        
        Args:
            gd: Datos del generador
            base_flow: Flujo base sin GD
            
        Returns:
            Reducción estimada en MW
        """
        # Encontrar tramos afectados por el GD
        affected_sections = []
        gd_location_km = next(s['distance_km'] for s in self.stations if s['name'] == gd['station'])
        
        for flow in base_flow:
            # Verificar si el tramo está aguas arriba del GD
            from_km = next(s['distance_km'] for s in self.stations if s['name'] == flow['from'])
            to_km = next(s['distance_km'] for s in self.stations if s['name'] == flow['to'])
            
            if from_km <= gd_location_km <= to_km or to_km <= gd_location_km <= from_km:
                affected_sections.append(flow)
        
        # Estimar reducción (simplificado: proporcional a P²)
        local_reduction = 0
        for section in affected_sections:
            # Reducción aproximada: 2 * P_gd * P_flujo / P_total * pérdidas_unitarias
            p_ratio = min(gd['p_mw'] / section['p_mw'], 1.0) if section['p_mw'] > 0 else 0
            section_losses = section['p_mw']**2 * 0.001  # Pérdidas unitarias estimadas
            local_reduction += p_ratio * section_losses
        
        return local_reduction
    
    def optimal_gd_placement(self, candidate_locations: List[str], gd_size_mw: float) -> Dict:
        """
        Encuentra ubicación óptima para GD de tamaño dado
        
        Args:
            candidate_locations: Lista de estaciones candidatas
            gd_size_mw: Tamaño del GD a ubicar
            
        Returns:
            Diccionario con análisis de ubicaciones
        """
        # Perfil de carga típico
        typical_load = {
            'Pilcaniyeu': {'p_mw': 0},
            'Jacobacci': {'p_mw': 1.45},
            'Maquinchao': {'p_mw': 0.50},
            'Los Menucos': {'p_mw': 1.40}
        }
        
        results = []
        
        for location in candidate_locations:
            # Simular GD en esta ubicación
            gd_config = [{
                'station': location,
                'p_mw': gd_size_mw,
                'location_km': next(s['distance_km'] for s in self.stations if s['name'] == location)
            }]
            
            analysis = self.simulate_gd_injection(gd_config, typical_load)
            
            results.append({
                'location': location,
                'loss_reduction_mw': analysis['reduction']['loss_reduction_mw'],
                'loss_reduction_percent': analysis['reduction']['loss_reduction_percent'],
                'annual_savings_usd': analysis['reduction']['annual_value_usd'],
                'efficiency_ratio': analysis['reduction']['loss_reduction_mw'] / gd_size_mw
            })
        
        # Ordenar por eficiencia
        results.sort(key=lambda x: x['efficiency_ratio'], reverse=True)
        
        return {
            'optimal_location': results[0]['location'],
            'ranking': results,
            'best_reduction_mw': results[0]['loss_reduction_mw'],
            'best_annual_savings': results[0]['annual_savings_usd']
        }


# Configuración de red Línea Sur
NETWORK_CONFIG = {
    'stations': [
        {'name': 'Pilcaniyeu', 'distance_km': 0},
        {'name': 'Jacobacci', 'distance_km': 150},
        {'name': 'Maquinchao', 'distance_km': 210},
        {'name': 'Los Menucos', 'distance_km': 270}
    ],
    'conductor_data': {
        'Pilcaniyeu_Jacobacci': {
            'r_ohm_per_km': 0.245,
            'x_ohm_per_km': 0.410,
            'length_km': 150,
            'type': '120 Al/Al'
        },
        'Jacobacci_Maquinchao': {
            'r_ohm_per_km': 0.420,
            'x_ohm_per_km': 0.425,
            'length_km': 60,
            'type': '70 Al/Al'
        },
        'Maquinchao_Los Menucos': {
            'r_ohm_per_km': 0.420,
            'x_ohm_per_km': 0.425,
            'length_km': 60,
            'type': '70 Al/Al'
        }
    },
    'base_mva': 100,
    'voltage_kv': 33
}


# Ejemplo de uso
if __name__ == "__main__":
    calculator = LossReductionCalculator(NETWORK_CONFIG)
    
    print("=== ANÁLISIS REDUCCIÓN DE PÉRDIDAS - LÍNEA SUR ===\n")
    
    # Caso 1: Solo Los Menucos (3 MW)
    print("1. CASO LOS MENUCOS (3 MW):")
    gd_menucos = [{'station': 'Los Menucos', 'p_mw': 3.0, 'location_km': 270}]
    load_profile = {
        'Jacobacci': {'p_mw': 1.45},
        'Maquinchao': {'p_mw': 0.50},
        'Los Menucos': {'p_mw': 1.40}
    }
    
    result_menucos = calculator.simulate_gd_injection(gd_menucos, load_profile)
    print(f"   - Pérdidas sin GD: {result_menucos['base_case']['total_losses_mw']:.2f} MW ({result_menucos['base_case']['losses_percent']:.1f}%)")
    print(f"   - Pérdidas con GD: {result_menucos['gd_case']['total_losses_mw']:.2f} MW ({result_menucos['gd_case']['losses_percent']:.1f}%)")
    print(f"   - Reducción: {result_menucos['reduction']['loss_reduction_mw']:.2f} MW ({result_menucos['reduction']['loss_reduction_percent']:.1f}%)")
    print(f"   - Ahorro anual: ${result_menucos['reduction']['annual_value_usd']:,.0f}")
    
    # Caso 2: Solo Jacobacci (1 MW)
    print("\n2. CASO JACOBACCI (1 MW):")
    gd_jacobacci = [{'station': 'Jacobacci', 'p_mw': 1.0, 'location_km': 150}]
    
    result_jacobacci = calculator.simulate_gd_injection(gd_jacobacci, load_profile)
    print(f"   - Pérdidas sin GD: {result_jacobacci['base_case']['total_losses_mw']:.2f} MW")
    print(f"   - Pérdidas con GD: {result_jacobacci['gd_case']['total_losses_mw']:.2f} MW")
    print(f"   - Reducción: {result_jacobacci['reduction']['loss_reduction_mw']:.2f} MW ({result_jacobacci['reduction']['loss_reduction_percent']:.1f}%)")
    print(f"   - Ahorro anual: ${result_jacobacci['reduction']['annual_value_usd']:,.0f}")
    
    # Caso 3: Ambos proyectos
    print("\n3. CASO COMBINADO (Los Menucos 3 MW + Jacobacci 1 MW):")
    gd_combined = [
        {'station': 'Los Menucos', 'p_mw': 3.0, 'location_km': 270},
        {'station': 'Jacobacci', 'p_mw': 1.0, 'location_km': 150}
    ]
    
    result_combined = calculator.simulate_gd_injection(gd_combined, load_profile)
    print(f"   - Pérdidas sin GD: {result_combined['base_case']['total_losses_mw']:.2f} MW")
    print(f"   - Pérdidas con GD: {result_combined['gd_case']['total_losses_mw']:.2f} MW")
    print(f"   - Reducción total: {result_combined['reduction']['loss_reduction_mw']:.2f} MW ({result_combined['reduction']['loss_reduction_percent']:.1f}%)")
    print(f"   - Ahorro anual: ${result_combined['reduction']['annual_value_usd']:,.0f}")
    
    print("\n   Impacto por proyecto:")
    for impact in result_combined['gd_impact']:
        print(f"   - {impact['location']}: {impact['local_loss_reduction_mw']:.3f} MW reducidos")
    
    # Análisis de ubicación óptima
    print("\n4. ANÁLISIS UBICACIÓN ÓPTIMA (1 MW):")
    optimal = calculator.optimal_gd_placement(['Jacobacci', 'Maquinchao', 'Los Menucos'], 1.0)
    print(f"   - Ubicación óptima: {optimal['optimal_location']}")
    print(f"   - Reducción máxima: {optimal['best_reduction_mw']:.3f} MW")
    print(f"   - Ahorro máximo: ${optimal['best_annual_savings']:,.0f}/año")
    
    print("\n   Ranking completo:")
    for i, loc in enumerate(optimal['ranking']):
        print(f"   {i+1}. {loc['location']}: {loc['loss_reduction_mw']:.3f} MW ({loc['efficiency_ratio']:.2f} MW red/MW gen)")
    
    # Resumen beneficios totales
    print("\n5. RESUMEN BENEFICIOS POR REDUCCIÓN DE PÉRDIDAS:")
    total_loss_reduction = result_combined['reduction']['loss_reduction_mw']
    total_energy_saved = result_combined['reduction']['annual_energy_saved_mwh']
    total_value = result_combined['reduction']['annual_value_usd']
    
    print(f"   - Reducción pérdidas totales: {total_loss_reduction:.2f} MW")
    print(f"   - Energía ahorrada anual: {total_energy_saved:,.0f} MWh")
    print(f"   - Valor económico anual: ${total_value:,.0f}")
    print(f"   - CO₂ evitado: {total_energy_saved * 0.5:,.0f} ton/año")
    print(f"   - Equivalente hogares: {total_energy_saved / 3.5:,.0f} hogares/año")