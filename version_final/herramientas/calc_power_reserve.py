#!/usr/bin/env python3
"""
calc_power_reserve.py
Herramienta para calcular reserva de potencia con BESS - Los Menucos
Reemplazo del generador diesel (10 min/día operación promedio)
"""

import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Tuple

class PowerReserveCalculator:
    """Calculadora para reserva de potencia con BESS"""
    
    def __init__(self, config: Dict):
        """
        Inicializa calculadora con configuración del sistema
        
        Args:
            config: Diccionario con parámetros del sistema
                - diesel_mw: Potencia diesel actual
                - diesel_minutes_day: Minutos operación/día promedio
                - bess_mwh: Capacidad BESS propuesta
                - bess_mw: Potencia BESS propuesta
                - diesel_cost_usd_mwh: Costo generación diesel
                - diesel_rental_usd_year: Costo fijo alquiler anual
                - bess_cycles_year: Ciclos esperados/año
        """
        self.diesel_mw = config['diesel_mw']
        self.diesel_minutes_day = config['diesel_minutes_day']
        self.bess_mwh = config['bess_mwh']
        self.bess_mw = config['bess_mw']
        self.diesel_cost = config['diesel_cost_usd_mwh']
        self.diesel_rental = config.get('diesel_rental_usd_year', 0)
        self.bess_cycles_year = config['bess_cycles_year']
        
        # Parámetros BESS
        self.soc_min = 0.10
        self.soc_max = 0.95
        self.efficiency = 0.92
        self.response_time_ms = 100
        
    def calculate_reserve_capacity(self) -> Dict:
        """
        Calcula capacidad de reserva del BESS vs diesel
        
        Returns:
            Diccionario con análisis de capacidad
        """
        # Energía diesel diaria promedio
        diesel_energy_daily = self.diesel_mw * (self.diesel_minutes_day / 60)
        
        # Energía útil BESS
        bess_usable_energy = self.bess_mwh * (self.soc_max - self.soc_min) * self.efficiency
        
        # Duración a potencia nominal
        duration_at_nominal = (bess_usable_energy / self.bess_mw) * 60  # minutos
        
        # Duración equivalente a diesel
        duration_at_diesel = (bess_usable_energy / self.diesel_mw) * 60  # minutos
        
        # Eventos que puede cubrir
        events_per_charge = duration_at_diesel / self.diesel_minutes_day
        
        results = {
            'diesel_daily_energy_mwh': diesel_energy_daily,
            'diesel_annual_energy_mwh': diesel_energy_daily * 365,
            'bess_usable_energy_mwh': bess_usable_energy,
            'duration_at_nominal_min': duration_at_nominal,
            'duration_at_diesel_power_min': duration_at_diesel,
            'events_per_charge': events_per_charge,
            'reserve_factor': duration_at_diesel / self.diesel_minutes_day,
            'response_improvement': f"{self.diesel_mw * 1000 / 60:.0f}x faster"  # MW/min vs MW/100ms
        }
        
        return results
    
    def analyze_event_patterns(self) -> Dict:
        """
        Analiza patrones típicos de eventos que requieren reserva
        
        Returns:
            Diccionario con análisis de eventos
        """
        # Eventos típicos basados en 10 min/día promedio
        event_patterns = {
            'voltage_collapse': {
                'duration_min': 2,
                'power_mw': self.diesel_mw,
                'frequency_per_month': 8,
                'criticality': 'high'
            },
            'peak_shaving': {
                'duration_min': 15,
                'power_mw': self.diesel_mw * 0.7,
                'frequency_per_month': 4,
                'criticality': 'medium'
            },
            'contingency_n1': {
                'duration_min': 30,
                'power_mw': self.diesel_mw * 0.5,
                'frequency_per_month': 2,
                'criticality': 'high'
            },
            'maintenance_window': {
                'duration_min': 60,
                'power_mw': self.diesel_mw * 0.3,
                'frequency_per_month': 1,
                'criticality': 'low'
            }
        }
        
        total_minutes_month = 0
        total_energy_month = 0
        
        for event, data in event_patterns.items():
            minutes = data['duration_min'] * data['frequency_per_month']
            energy = data['power_mw'] * minutes / 60
            total_minutes_month += minutes
            total_energy_month += energy
            
            data['monthly_minutes'] = minutes
            data['monthly_energy_mwh'] = energy
            data['bess_can_cover'] = data['duration_min'] <= self.calculate_reserve_capacity()['duration_at_diesel_power_min']
        
        # Validar contra promedio real (10 min/día = 300 min/mes)
        scale_factor = 300 / total_minutes_month
        
        # Ajustar frecuencias para coincidir con realidad
        for event in event_patterns.values():
            event['frequency_per_month'] *= scale_factor
            event['monthly_minutes'] *= scale_factor
            event['monthly_energy_mwh'] *= scale_factor
        
        return event_patterns
    
    def economic_comparison(self) -> Dict:
        """
        Compara economía diesel vs BESS para reserva
        
        Returns:
            Diccionario con comparación económica
        """
        # Costos diesel actuales
        diesel_energy_year = self.diesel_mw * (self.diesel_minutes_day / 60) * 365
        diesel_fuel_cost = diesel_energy_year * self.diesel_cost
        diesel_maintenance = 15000  # USD/año O&M estimado
        diesel_total_annual = self.diesel_rental + diesel_fuel_cost + diesel_maintenance
        
        # Costo real por MWh de reserva
        diesel_cost_per_mwh = diesel_total_annual / diesel_energy_year if diesel_energy_year > 0 else 0
        
        # Costos BESS para misma función
        bess_cycles = self.bess_cycles_year
        bess_energy_cycled = bess_cycles * self.bess_mwh * (self.soc_max - self.soc_min)
        bess_losses = bess_energy_cycled * (1 - self.efficiency)
        bess_energy_cost = bess_losses * 71  # USD/MWh tarifa actualizada
        bess_maintenance = self.bess_mwh * 5 * 1000  # $5/kWh-año
        bess_total_annual = bess_energy_cost + bess_maintenance
        
        # Beneficios adicionales BESS
        faster_response_value = 10000  # USD/año por respuesta instantánea
        no_emissions_value = diesel_energy_year * 0.5 * 50  # 0.5 tCO2/MWh @ $50/tCO2
        
        results = {
            'diesel_costs': {
                'rental_usd_year': self.diesel_rental,
                'fuel_usd_year': diesel_fuel_cost,
                'maintenance_usd_year': diesel_maintenance,
                'total_usd_year': diesel_total_annual,
                'cost_per_mwh': diesel_cost_per_mwh
            },
            'bess_costs': {
                'energy_losses_usd_year': bess_energy_cost,
                'maintenance_usd_year': bess_maintenance,
                'total_usd_year': bess_total_annual
            },
            'bess_benefits': {
                'faster_response_usd_year': faster_response_value,
                'emissions_avoided_usd_year': no_emissions_value,
                'total_additional_usd_year': faster_response_value + no_emissions_value
            },
            'net_annual_benefit': diesel_total_annual - bess_total_annual + faster_response_value + no_emissions_value
        }
        
        return results
    
    def reliability_improvement(self) -> Dict:
        """
        Calcula mejora en confiabilidad con BESS vs diesel
        
        Returns:
            Diccionario con métricas de confiabilidad
        """
        # Tiempos típicos
        diesel_start_time_min = 5  # Tiempo arranque diesel
        diesel_sync_time_min = 2   # Tiempo sincronización
        diesel_total_response = diesel_start_time_min + diesel_sync_time_min
        
        bess_response_time_sec = self.response_time_ms / 1000
        
        # Disponibilidad
        diesel_availability = 0.95  # 95% típico
        diesel_fail_to_start = 0.02  # 2% falla arranque
        
        bess_availability = 0.98  # 98% típico
        bess_fail_rate = 0.001  # 0.1% falla
        
        # Energía no suministrada evitada
        load_lost_during_start = self.diesel_mw * (diesel_total_response / 60)  # MWh
        events_per_year = self.diesel_minutes_day * 365 / 10  # asumiendo eventos de 10 min
        ens_avoided = load_lost_during_start * events_per_year * diesel_fail_to_start
        
        results = {
            'response_time': {
                'diesel_minutes': diesel_total_response,
                'bess_seconds': bess_response_time_sec,
                'improvement_factor': diesel_total_response * 60 / bess_response_time_sec
            },
            'availability': {
                'diesel_percent': diesel_availability * 100,
                'bess_percent': bess_availability * 100,
                'improvement_pp': (bess_availability - diesel_availability) * 100
            },
            'reliability': {
                'diesel_fail_to_start': diesel_fail_to_start * 100,
                'bess_fail_rate': bess_fail_rate * 100,
                'mtbf_improvement': f"{(1/bess_fail_rate)/(1/diesel_fail_to_start):.0f}x"
            },
            'ens_metrics': {
                'ens_per_event_mwh': load_lost_during_start,
                'events_per_year': events_per_year,
                'ens_avoided_mwh_year': ens_avoided,
                'ens_value_usd_year': ens_avoided * 200  # $200/MWh ENS
            }
        }
        
        return results


# Ejemplo de uso
if __name__ == "__main__":
    # Configuración Los Menucos basada en datos reales
    config = {
        'diesel_mw': 1.8,  # Generador diesel actual
        'diesel_minutes_day': 10,  # Operación promedio real
        'bess_mwh': 2.0,  # BESS propuesto
        'bess_mw': 1.5,   # Potencia BESS
        'diesel_cost_usd_mwh': 125,  # Costo diesel
        'diesel_rental_usd_year': 190000,  # Alquiler fijo anual
        'bess_cycles_year': 365  # 1 ciclo/día promedio
    }
    
    calculator = PowerReserveCalculator(config)
    
    print("=== ANÁLISIS RESERVA DE POTENCIA - LOS MENUCOS ===\n")
    print("Configuración actual: Diesel 1.8 MW operando 10 min/día promedio\n")
    
    # Capacidad de reserva
    print("1. CAPACIDAD DE RESERVA BESS:")
    capacity = calculator.calculate_reserve_capacity()
    print(f"   - Energía diesel diaria: {capacity['diesel_daily_energy_mwh']:.2f} MWh")
    print(f"   - Energía útil BESS: {capacity['bess_usable_energy_mwh']:.2f} MWh")
    print(f"   - Duración a 1.8 MW: {capacity['duration_at_diesel_power_min']:.0f} minutos")
    print(f"   - Factor de reserva: {capacity['reserve_factor']:.1f}x requerimiento diario")
    print(f"   - Mejora respuesta: {capacity['response_improvement']}")
    
    # Patrones de eventos
    print("\n2. ANÁLISIS DE EVENTOS TÍPICOS:")
    events = calculator.analyze_event_patterns()
    for event_name, data in events.items():
        print(f"\n   {event_name.replace('_', ' ').title()}:")
        print(f"   - Duración: {data['duration_min']} min @ {data['power_mw']:.1f} MW")
        print(f"   - Frecuencia: {data['frequency_per_month']:.1f} eventos/mes")
        print(f"   - BESS puede cubrir: {'SÍ' if data['bess_can_cover'] else 'NO'}")
    
    # Comparación económica
    print("\n3. COMPARACIÓN ECONÓMICA ANUAL:")
    economics = calculator.economic_comparison()
    print(f"   Costos Diesel:")
    print(f"   - Alquiler fijo: ${economics['diesel_costs']['rental_usd_year']:,.0f}")
    print(f"   - Combustible: ${economics['diesel_costs']['fuel_usd_year']:,.0f}")
    print(f"   - Mantenimiento: ${economics['diesel_costs']['maintenance_usd_year']:,.0f}")
    print(f"   - TOTAL: ${economics['diesel_costs']['total_usd_year']:,.0f}")
    print(f"   - Costo real/MWh: ${economics['diesel_costs']['cost_per_mwh']:,.0f}")
    
    print(f"\n   Costos BESS:")
    print(f"   - Pérdidas energía: ${economics['bess_costs']['energy_losses_usd_year']:,.0f}")
    print(f"   - Mantenimiento: ${economics['bess_costs']['maintenance_usd_year']:,.0f}")
    print(f"   - TOTAL: ${economics['bess_costs']['total_usd_year']:,.0f}")
    
    print(f"\n   Beneficios adicionales BESS:")
    print(f"   - Respuesta rápida: ${economics['bess_benefits']['faster_response_usd_year']:,.0f}")
    print(f"   - Emisiones evitadas: ${economics['bess_benefits']['emissions_avoided_usd_year']:,.0f}")
    
    print(f"\n   BENEFICIO NETO ANUAL: ${economics['net_annual_benefit']:,.0f}")
    
    # Mejora confiabilidad
    print("\n4. MEJORA EN CONFIABILIDAD:")
    reliability = calculator.reliability_improvement()
    print(f"   Tiempo de respuesta:")
    print(f"   - Diesel: {reliability['response_time']['diesel_minutes']} minutos")
    print(f"   - BESS: {reliability['response_time']['bess_seconds']:.1f} segundos")
    print(f"   - Mejora: {reliability['response_time']['improvement_factor']:.0f}x más rápido")
    
    print(f"\n   Disponibilidad:")
    print(f"   - Diesel: {reliability['availability']['diesel_percent']:.1f}%")
    print(f"   - BESS: {reliability['availability']['bess_percent']:.1f}%")
    
    print(f"\n   ENS evitada:")
    print(f"   - {reliability['ens_metrics']['ens_avoided_mwh_year']:.1f} MWh/año")
    print(f"   - Valor: ${reliability['ens_metrics']['ens_value_usd_year']:,.0f}/año")