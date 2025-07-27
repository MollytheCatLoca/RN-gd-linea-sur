#!/usr/bin/env python3
"""
calc_q_at_night.py
Herramienta para calcular beneficios de Q nocturno (STATCOM mode)
Aplicable tanto a Los Menucos como Jacobacci
"""

import numpy as np
from typing import Dict, List, Tuple
import math

class QAtNightCalculator:
    """Calculadora para compensación reactiva nocturna usando inversores FV"""
    
    def __init__(self, config: Dict):
        """
        Inicializa calculadora con configuración del sistema
        
        Args:
            config: Diccionario con parámetros
                - inverter_mva: Capacidad inversores en MVA
                - location: 'los_menucos' o 'jacobacci'
                - line_length_km: Longitud de línea hasta fuente
                - night_load_mw: Carga nocturna promedio
                - current_pf: Factor de potencia actual
                - voltage_pu: Voltaje actual en pu
        """
        self.inverter_mva = config['inverter_mva']
        self.location = config['location']
        self.line_length = config['line_length_km']
        self.night_load_mw = config['night_load_mw']
        self.current_pf = config['current_pf']
        self.voltage_pu = config['voltage_pu']
        
        # Parámetros de línea (33kV)
        self.r_ohm_per_km = 0.3  # Resistencia promedio
        self.x_ohm_per_km = 0.4  # Reactancia promedio
        self.v_base_kv = 33
        self.s_base_mva = 100
        
    def calculate_q_capability(self, solar_p_mw: float = 0) -> Dict:
        """
        Calcula capacidad Q disponible del inversor
        
        Args:
            solar_p_mw: Potencia activa solar (0 para nocturno)
            
        Returns:
            Diccionario con capacidad Q
        """
        # Capacidad Q según curva PQ del inversor
        if solar_p_mw == 0:  # Modo STATCOM puro nocturno
            q_available = self.inverter_mva  # 100% disponible
            mode = "STATCOM puro"
        else:
            # Q disponible = sqrt(S² - P²)
            q_available = math.sqrt(max(0, self.inverter_mva**2 - solar_p_mw**2))
            mode = "PV+Q"
        
        # Limitaciones prácticas
        q_max_cap = q_available  # Capacitivo
        q_max_ind = q_available * 0.95  # Inductivo (95% por estabilidad)
        
        # Operación conservadora
        q_operating_cap = q_max_cap * 0.35  # 35% para margen
        q_operating_ind = q_max_ind * 0.35
        
        return {
            'mode': mode,
            'q_max_capacitive_mvar': q_max_cap,
            'q_max_inductive_mvar': q_max_ind,
            'q_operating_cap_mvar': q_operating_cap,
            'q_operating_ind_mvar': q_operating_ind,
            'utilization_percent': (solar_p_mw / self.inverter_mva * 100) if self.inverter_mva > 0 else 0
        }
    
    def calculate_power_factor_improvement(self, q_injection_mvar: float) -> Dict:
        """
        Calcula mejora en factor de potencia con inyección Q
        
        Args:
            q_injection_mvar: Potencia reactiva a inyectar (+ capacitiva)
            
        Returns:
            Diccionario con mejora de FP
        """
        # Potencia aparente actual
        s_current = self.night_load_mw / self.current_pf
        q_current = math.sqrt(s_current**2 - self.night_load_mw**2)
        
        # Nueva Q después de compensación
        q_new = q_current - q_injection_mvar  # Resta porque inyección capacitiva reduce Q inductiva
        
        # Nueva potencia aparente
        s_new = math.sqrt(self.night_load_mw**2 + q_new**2)
        
        # Nuevo factor de potencia
        pf_new = self.night_load_mw / s_new if s_new > 0 else 1.0
        
        # Reducción de corriente
        current_reduction = (1 - s_new/s_current) * 100
        
        return {
            'pf_original': self.current_pf,
            'pf_new': min(pf_new, 1.0),
            'pf_improvement': min(pf_new, 1.0) - self.current_pf,
            's_original_mva': s_current,
            's_new_mva': s_new,
            'current_reduction_percent': max(0, current_reduction),
            'q_load_original_mvar': q_current,
            'q_load_new_mvar': q_new
        }
    
    def calculate_loss_reduction(self, q_injection_mvar: float) -> Dict:
        """
        Calcula reducción de pérdidas I²R con compensación Q
        
        Args:
            q_injection_mvar: Potencia reactiva a inyectar
            
        Returns:
            Diccionario con reducción de pérdidas
        """
        # Impedancia de línea
        z_base = self.v_base_kv**2 / self.s_base_mva
        r_pu = self.r_ohm_per_km * self.line_length / z_base
        
        # Corriente antes y después
        pf_analysis = self.calculate_power_factor_improvement(q_injection_mvar)
        i_ratio = pf_analysis['s_new_mva'] / pf_analysis['s_original_mva']
        
        # Pérdidas I²R
        # P_loss = I² * R, entonces nueva pérdida = (I_new/I_old)² * P_loss_old
        loss_reduction_factor = 1 - i_ratio**2
        
        # Pérdidas actuales estimadas
        current_losses_mw = (pf_analysis['s_original_mva'] / self.voltage_pu)**2 * r_pu
        new_losses_mw = current_losses_mw * i_ratio**2
        
        # Energía ahorrada (asumiendo operación nocturna 10h/día)
        night_hours = 10
        energy_saved_daily = (current_losses_mw - new_losses_mw) * night_hours
        energy_saved_annual = energy_saved_daily * 365
        
        # Valor económico
        energy_value_usd_mwh = 122.7  # Costo de pérdidas
        annual_savings_usd = energy_saved_annual * energy_value_usd_mwh
        
        return {
            'current_losses_kw': current_losses_mw * 1000,
            'new_losses_kw': new_losses_mw * 1000,
            'loss_reduction_kw': (current_losses_mw - new_losses_mw) * 1000,
            'loss_reduction_percent': loss_reduction_factor * 100,
            'energy_saved_mwh_year': energy_saved_annual,
            'savings_usd_year': annual_savings_usd,
            'co2_avoided_ton_year': energy_saved_annual * 0.5  # 0.5 tCO2/MWh
        }
    
    def calculate_voltage_improvement(self, q_injection_mvar: float) -> Dict:
        """
        Calcula mejora de voltaje con compensación Q
        
        Args:
            q_injection_mvar: Potencia reactiva a inyectar
            
        Returns:
            Diccionario con mejora de voltaje
        """
        # Sensibilidad dV/dQ aproximada
        x_pu = self.x_ohm_per_km * self.line_length * self.s_base_mva / self.v_base_kv**2
        dv_dq = x_pu / self.voltage_pu  # pu/MVAr
        
        # Mejora de voltaje
        voltage_improvement_pu = q_injection_mvar * dv_dq / self.s_base_mva
        new_voltage_pu = self.voltage_pu + voltage_improvement_pu
        
        # Beneficios por mejor voltaje
        voltage_benefits = {
            'equipment_life_extension': voltage_improvement_pu > 0.02,  # 2% mejora significativa
            'motor_efficiency_gain': voltage_improvement_pu * 0.5 * 100,  # % eficiencia
            'lighting_improvement': voltage_improvement_pu > 0.03,  # 3% mejora notable
        }
        
        return {
            'voltage_original_pu': self.voltage_pu,
            'voltage_new_pu': new_voltage_pu,
            'voltage_improvement_pu': voltage_improvement_pu,
            'voltage_improvement_percent': (voltage_improvement_pu / self.voltage_pu) * 100,
            'benefits': voltage_benefits,
            'regulation_compliance': new_voltage_pu >= 0.95  # Cumple regulación
        }
    
    def optimal_q_schedule(self) -> Dict:
        """
        Genera programa óptimo de Q para 24 horas
        
        Returns:
            Diccionario con programa horario
        """
        # Perfiles típicos por hora
        load_profile = {
            'los_menucos': [0.5, 0.5, 0.5, 0.5, 0.5, 0.6,  # 00-05h
                           0.7, 0.8, 0.9, 0.9, 0.9, 0.9,   # 06-11h
                           0.9, 0.9, 0.9, 0.9, 1.0, 1.2,   # 12-17h
                           1.4, 1.5, 1.4, 1.2, 0.9, 0.7],  # 18-23h
            'jacobacci': [0.4, 0.4, 0.4, 0.4, 0.4, 0.5,    # Perfil más plano
                         0.6, 0.7, 0.8, 0.8, 0.8, 0.8,
                         0.8, 0.8, 0.8, 0.8, 0.9, 1.0,
                         1.1, 1.2, 1.1, 1.0, 0.7, 0.5]
        }
        
        solar_profile = [0, 0, 0, 0, 0, 0,  # 00-05h
                        0.1, 0.3, 0.5, 0.7, 0.9, 0.95,  # 06-11h
                        1.0, 0.95, 0.9, 0.7, 0.5, 0.2,  # 12-17h
                        0.05, 0, 0, 0, 0, 0]  # 18-23h
        
        schedule = []
        total_q_mvarh = 0
        
        for hour in range(24):
            solar_pu = solar_profile[hour]
            load_pu = load_profile[self.location][hour]
            
            # Calcular Q disponible
            solar_mw = solar_pu * (3.0 if self.location == 'los_menucos' else 1.0)
            q_cap = self.calculate_q_capability(solar_mw)
            
            # Estrategia Q
            if hour >= 20 or hour < 6:  # Nocturno 20-06h
                q_mode = "STATCOM"
                q_setpoint = q_cap['q_operating_cap_mvar']
            elif solar_pu > 0.8:  # Solar alto
                q_mode = "Unity PF"
                q_setpoint = 0
            else:  # Transición
                q_mode = "Q(V)"
                q_setpoint = q_cap['q_operating_cap_mvar'] * (1 - solar_pu)
            
            total_q_mvarh += q_setpoint
            
            schedule.append({
                'hour': hour,
                'solar_mw': solar_mw,
                'load_mw': load_pu * self.night_load_mw / 0.5,  # Escalado desde load nocturno
                'q_available_mvar': q_cap['q_max_capacitive_mvar'],
                'q_setpoint_mvar': q_setpoint,
                'q_mode': q_mode
            })
        
        return {
            'hourly_schedule': schedule,
            'total_q_mvarh_day': total_q_mvarh,
            'night_hours_statcom': sum(1 for h in schedule if h['q_mode'] == 'STATCOM'),
            'average_q_night_mvar': np.mean([h['q_setpoint_mvar'] for h in schedule if h['hour'] >= 20 or h['hour'] < 6])
        }


# Ejemplo de uso
if __name__ == "__main__":
    # Configuración para ambas ubicaciones
    configs = {
        'los_menucos': {
            'inverter_mva': 3.0,  # 3 MVA para 3 MW FV
            'location': 'los_menucos',
            'line_length_km': 270,
            'night_load_mw': 0.55,
            'current_pf': 0.78,  # Dato real nocturno
            'voltage_pu': 0.237
        },
        'jacobacci': {
            'inverter_mva': 1.2,  # 1.2 MVA para 1 MW FV
            'location': 'jacobacci',
            'line_length_km': 150,
            'night_load_mw': 0.45,
            'current_pf': 0.985,  # Mejor que Los Menucos
            'voltage_pu': 0.245
        }
    }
    
    for location, config in configs.items():
        calculator = QAtNightCalculator(config)
        
        print(f"\n{'='*60}")
        print(f"ANÁLISIS Q AT NIGHT - {location.upper()}")
        print(f"{'='*60}\n")
        
        # Capacidad Q nocturna
        print("1. CAPACIDAD Q NOCTURNA (STATCOM PURO):")
        q_cap = calculator.calculate_q_capability(0)
        print(f"   - Capacidad máxima: ±{q_cap['q_max_capacitive_mvar']:.1f} MVAr")
        print(f"   - Operación conservadora: ±{q_cap['q_operating_cap_mvar']:.2f} MVAr")
        print(f"   - Modo: {q_cap['mode']}")
        
        # Usar Q operacional para análisis
        q_injection = q_cap['q_operating_cap_mvar']
        
        # Mejora factor de potencia
        print(f"\n2. MEJORA FACTOR DE POTENCIA (con {q_injection:.2f} MVAr):")
        pf_improvement = calculator.calculate_power_factor_improvement(q_injection)
        print(f"   - FP actual: {pf_improvement['pf_original']:.3f}")
        print(f"   - FP mejorado: {pf_improvement['pf_new']:.3f}")
        print(f"   - Reducción corriente: {pf_improvement['current_reduction_percent']:.1f}%")
        
        # Reducción pérdidas
        print(f"\n3. REDUCCIÓN PÉRDIDAS I²R:")
        losses = calculator.calculate_loss_reduction(q_injection)
        print(f"   - Pérdidas actuales: {losses['current_losses_kw']:.0f} kW")
        print(f"   - Pérdidas nuevas: {losses['new_losses_kw']:.0f} kW")
        print(f"   - Reducción: {losses['loss_reduction_percent']:.1f}%")
        print(f"   - Ahorro anual: {losses['energy_saved_mwh_year']:.0f} MWh")
        print(f"   - Valor económico: ${losses['savings_usd_year']:,.0f}/año")
        
        # Mejora voltaje
        print(f"\n4. MEJORA DE VOLTAJE:")
        voltage = calculator.calculate_voltage_improvement(q_injection)
        print(f"   - Voltaje actual: {voltage['voltage_original_pu']:.3f} pu")
        print(f"   - Voltaje mejorado: {voltage['voltage_new_pu']:.3f} pu")
        print(f"   - Mejora: +{voltage['voltage_improvement_percent']:.1f}%")
        print(f"   - Cumple regulación (>0.95 pu): {'SÍ' if voltage['regulation_compliance'] else 'NO'}")
        
        # Programa 24h
        print(f"\n5. PROGRAMA Q ÓPTIMO 24H:")
        schedule = calculator.optimal_q_schedule()
        print(f"   - Horas en modo STATCOM: {schedule['night_hours_statcom']}")
        print(f"   - Q promedio nocturno: {schedule['average_q_night_mvar']:.2f} MVAr")
        print(f"   - Energía reactiva total: {schedule['total_q_mvarh_day']:.0f} MVArh/día")
        
        # Resumen beneficios anuales
        annual_benefits = (losses['savings_usd_year'] + 
                          (10000 if voltage['voltage_improvement_percent'] > 5 else 5000))  # Valor mejora voltaje
        
        print(f"\n6. BENEFICIOS TOTALES ANUALES:")
        print(f"   - Ahorro pérdidas: ${losses['savings_usd_year']:,.0f}")
        print(f"   - Mejora calidad voltaje: ${10000 if voltage['voltage_improvement_percent'] > 5 else 5000:,.0f}")
        print(f"   - CO₂ evitado: {losses['co2_avoided_ton_year']:.1f} ton/año")
        print(f"   - TOTAL: ${annual_benefits:,.0f}/año")