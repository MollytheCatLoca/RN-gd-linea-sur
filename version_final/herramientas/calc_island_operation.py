#!/usr/bin/env python3
"""
calc_island_operation.py
Herramienta para calcular capacidad de operación en isla - Los Menucos
"""

import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

class IslandOperationCalculator:
    """Calculadora para operación en isla con FV+BESS"""
    
    def __init__(self, config: Dict):
        """
        Inicializa calculadora con configuración del sistema
        
        Args:
            config: Diccionario con parámetros del sistema
                - pv_mw: Capacidad FV instalada
                - bess_mwh: Capacidad BESS en MWh
                - bess_mw: Potencia BESS en MW
                - load_critical_mw: Carga crítica
                - load_average_mw: Carga promedio
                - load_peak_mw: Carga pico
        """
        self.pv_mw = config['pv_mw']
        self.bess_mwh = config['bess_mwh']
        self.bess_mw = config['bess_mw']
        self.load_critical = config['load_critical_mw']
        self.load_average = config['load_average_mw']
        self.load_peak = config['load_peak_mw']
        
        # Parámetros BESS
        self.soc_min = 0.10
        self.soc_max = 0.95
        self.efficiency = 0.92
        
    def calculate_autonomy(self, load_mw: float, initial_soc: float = 0.8) -> float:
        """
        Calcula autonomía en horas para una carga dada
        
        Args:
            load_mw: Carga en MW
            initial_soc: Estado de carga inicial (0-1)
            
        Returns:
            Horas de autonomía
        """
        usable_energy = self.bess_mwh * (initial_soc - self.soc_min) * self.efficiency
        hours = usable_energy / load_mw if load_mw > 0 else float('inf')
        return hours
    
    def simulate_island_day(self, solar_profile: np.ndarray, load_profile: np.ndarray) -> Dict:
        """
        Simula operación en isla durante un día completo
        
        Args:
            solar_profile: Perfil solar horario (24 valores, MW)
            load_profile: Perfil de carga horario (24 valores, MW)
            
        Returns:
            Diccionario con resultados de simulación
        """
        hours = 24
        soc = np.zeros(hours + 1)
        soc[0] = 0.8  # SOC inicial 80%
        
        bess_power = np.zeros(hours)
        load_served = np.zeros(hours)
        load_shed = np.zeros(hours)
        
        for h in range(hours):
            # Balance de potencia
            net_load = load_profile[h] - solar_profile[h]
            
            if net_load > 0:  # Déficit - descarga BESS
                # Limitar por potencia y energía disponible
                max_discharge = min(self.bess_mw, 
                                  (soc[h] - self.soc_min) * self.bess_mwh * self.efficiency)
                
                bess_power[h] = -min(net_load, max_discharge)
                soc[h+1] = soc[h] + bess_power[h] / self.bess_mwh / self.efficiency
                
            else:  # Exceso - carga BESS
                # Limitar por potencia y capacidad restante
                max_charge = min(self.bess_mw, 
                               (self.soc_max - soc[h]) * self.bess_mwh / self.efficiency)
                
                bess_power[h] = min(-net_load, max_charge)
                soc[h+1] = soc[h] + bess_power[h] * self.efficiency / self.bess_mwh
            
            # Carga servida
            load_served[h] = min(load_profile[h], 
                               solar_profile[h] - bess_power[h])
            load_shed[h] = load_profile[h] - load_served[h]
        
        return {
            'soc': soc[:-1],
            'bess_power': bess_power,
            'load_served': load_served,
            'load_shed': load_shed,
            'total_shed_mwh': np.sum(load_shed),
            'min_soc': np.min(soc),
            'hours_survived': 24 if np.sum(load_shed) == 0 else np.argmax(load_shed > 0)
        }
    
    def critical_load_analysis(self) -> Dict:
        """
        Analiza capacidad de mantener cargas críticas
        
        Returns:
            Diccionario con análisis de cargas críticas
        """
        results = {}
        
        # Escenarios de carga crítica (% de carga promedio)
        critical_scenarios = [0.3, 0.4, 0.5, 0.6]
        
        for scenario in critical_scenarios:
            critical_load = self.load_average * scenario
            
            # Autonomía nocturna (sin FV)
            night_autonomy = self.calculate_autonomy(critical_load)
            
            # Autonomía con FV mínimo (10% capacidad)
            pv_min = self.pv_mw * 0.1
            day_autonomy = self.calculate_autonomy(critical_load - pv_min)
            
            results[f'critical_{int(scenario*100)}pct'] = {
                'load_mw': critical_load,
                'night_autonomy_hours': round(night_autonomy, 1),
                'day_autonomy_hours': round(day_autonomy, 1),
                'can_survive_24h': night_autonomy >= 12 and day_autonomy >= 12
            }
        
        return results
    
    def grid_forming_requirements(self) -> Dict:
        """
        Calcula requerimientos para operación grid-forming
        
        Returns:
            Diccionario con requerimientos técnicos
        """
        # Requerimientos de potencia instantánea
        inrush_factor = 3.0  # Factor de arranque motores
        motor_load = self.load_average * 0.3  # 30% carga motora estimada
        
        requirements = {
            'min_inverter_power_mw': self.load_peak * 1.2,  # 20% margen
            'min_inrush_capability_mw': motor_load * inrush_factor,
            'min_short_circuit_mva': self.load_peak * 5,  # Ratio típico
            'frequency_regulation': {
                'droop': '4%',
                'response_time_ms': 100,
                'deadband_hz': 0.1
            },
            'voltage_regulation': {
                'droop': '5%',
                'response_time_ms': 100,
                'deadband_pu': 0.01
            },
            'black_start_capable': True,
            'seamless_transfer': True
        }
        
        return requirements


# Ejemplo de uso
if __name__ == "__main__":
    # Configuración Los Menucos (Escenario 2)
    config = {
        'pv_mw': 3.0,
        'bess_mwh': 2.0,
        'bess_mw': 1.5,
        'load_critical_mw': 0.45,  # 50% de carga promedio
        'load_average_mw': 0.896,
        'load_peak_mw': 1.563
    }
    
    calculator = IslandOperationCalculator(config)
    
    print("=== ANÁLISIS OPERACIÓN EN ISLA - LOS MENUCOS ===\n")
    
    # Análisis de autonomía básica
    print("1. AUTONOMÍA BESS:")
    for load_name, load_mw in [('Crítica', config['load_critical_mw']),
                                ('Promedio', config['load_average_mw']),
                                ('Pico', config['load_peak_mw'])]:
        autonomy = calculator.calculate_autonomy(load_mw)
        print(f"   - Carga {load_name} ({load_mw:.2f} MW): {autonomy:.1f} horas")
    
    print("\n2. ANÁLISIS CARGAS CRÍTICAS:")
    critical_analysis = calculator.critical_load_analysis()
    for scenario, data in critical_analysis.items():
        print(f"   - {scenario}: {data['load_mw']:.2f} MW")
        print(f"     Autonomía nocturna: {data['night_autonomy_hours']} h")
        print(f"     Supervivencia 24h: {'SÍ' if data['can_survive_24h'] else 'NO'}")
    
    print("\n3. REQUERIMIENTOS GRID-FORMING:")
    requirements = calculator.grid_forming_requirements()
    print(f"   - Potencia inversores mínima: {requirements['min_inverter_power_mw']:.1f} MW")
    print(f"   - Capacidad arranque motores: {requirements['min_inrush_capability_mw']:.1f} MW")
    print(f"   - Cortocircuito mínimo: {requirements['min_short_circuit_mva']:.1f} MVA")
    print(f"   - Droop frecuencia: {requirements['frequency_regulation']['droop']}")
    print(f"   - Droop voltaje: {requirements['voltage_regulation']['droop']}")
    
    # Simulación día típico
    print("\n4. SIMULACIÓN DÍA EN ISLA:")
    # Perfil solar simplificado (MW)
    solar_profile = np.array([
        0, 0, 0, 0, 0, 0,  # 00-05h
        0.2, 0.8, 1.5, 2.2, 2.8, 2.9,  # 06-11h
        3.0, 2.9, 2.7, 2.3, 1.8, 1.0,  # 12-17h
        0.3, 0, 0, 0, 0, 0  # 18-23h
    ])
    
    # Perfil de carga típico (MW)
    load_profile = np.array([
        0.5, 0.5, 0.5, 0.5, 0.5, 0.6,  # 00-05h
        0.7, 0.8, 0.9, 0.9, 0.9, 0.9,  # 06-11h
        0.9, 0.9, 0.9, 0.9, 1.0, 1.2,  # 12-17h
        1.4, 1.5, 1.4, 1.2, 0.9, 0.7  # 18-23h
    ])
    
    sim_results = calculator.simulate_island_day(solar_profile, load_profile)
    
    print(f"   - Horas sobrevividas: {sim_results['hours_survived']}/24")
    print(f"   - Energía no servida: {sim_results['total_shed_mwh']:.2f} MWh")
    print(f"   - SOC mínimo: {sim_results['min_soc']*100:.1f}%")
    print(f"   - Viabilidad operación isla 24h: {'SÍ' if sim_results['hours_survived'] == 24 else 'NO'}")