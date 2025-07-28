# 02. ANÁLISIS TÉCNICO COMPARATIVO

## METODOLOGÍA DE ANÁLISIS

### Enfoque Sistémico
El análisis técnico se realizó considerando la red eléctrica como un sistema integrado, evaluando no solo la generación sino su impacto en:
- Flujos de potencia
- Perfiles de tensión
- Pérdidas técnicas
- Confiabilidad
- Flexibilidad operativa

### Herramientas Utilizadas
- **Flujo de carga**: Análisis en PSS/E
- **Optimización**: Algoritmos de ubicación óptima
- **Simulación solar**: PVsyst + perfiles horarios
- **Análisis económico**: Modelo propio en Python

## CONFIGURACIÓN CENTRALIZADA (BASE)

### Características del Parque Solar
```
ESPECIFICACIONES TÉCNICAS - MODELO CENTRALIZADO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Potencia DC:            14.64 MWp
Potencia AC:            11.5 MW
Tecnología:             Paneles bifaciales 550W
Configuración:          Trackers 1 eje N-S
Inversores:             Centrales 2.5 MW x 5
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Ubicación y Conexión
- **Sitio**: Terreno único de 25 hectáreas
- **Distancia a SE**: 2 km
- **Conexión**: Nueva línea 33 kV dedicada
- **Inversión conexión**: USD 1.5 millones

### Limitaciones Identificadas
1. **Punto único de falla**: Toda la generación en un sitio
2. **Sin servicios auxiliares**: Solo inyecta potencia activa
3. **Impacto local limitado**: No mejora calidad en la red
4. **Pérdidas de transmisión**: 2 km adicionales a 33 kV

## CONFIGURACIÓN DISTRIBUIDA MULTIPROPÓSITO

### Distribución de Capacidad
```
DISTRIBUCIÓN ESTRATÉGICA DE GENERACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Punto    Ubicación           Capacidad   Función
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
P1       SE Norte            3.0 MW      Principal
P2       Alim. Industrial    2.5 MW      Compensación
P3       Centro Comercial    2.0 MW      Respaldo
P4       Zona Turística      2.0 MW      Calidad
P5       Alim. Residencial   1.5 MW      Pérdidas
P6       SE Sur              1.5 MW      Regulación
P7       Parque Industrial   1.0 MW      Reactivo
P8       Zona Nueva          1.0 MW      Expansión
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL                        14.5 MW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Criterios de Selección de Puntos

#### 1. Maximización de Impacto (dV/dP)
```python
# Sensibilidad voltaje-potencia por punto
dV_dP = {
    'P1': 0.018,  # pu/MW - Moderado
    'P2': 0.025,  # pu/MW - Alto (industrial)
    'P3': 0.022,  # pu/MW - Alto
    'P4': 0.031,  # pu/MW - Muy alto (turismo)
    'P5': 0.028,  # pu/MW - Alto (residencial)
    'P6': 0.020,  # pu/MW - Moderado
    'P7': 0.024,  # pu/MW - Alto
    'P8': 0.035,  # pu/MW - Muy alto (punta)
}
```

#### 2. Reducción de Pérdidas
- Priorizar puntos con alta demanda local
- Minimizar flujos en alimentadores largos
- Balance entre fases
- Reducción de corrientes en troncales

#### 3. Mejora de Confiabilidad
- Redundancia distribuida (N-1 mejorado)
- Capacidad de isla intencional
- Respaldo ante contingencias
- Flexibilidad operativa

### Tecnología de Inversores
```
ESPECIFICACIONES INVERSORES DISTRIBUIDOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Tipo:               String, 4 cuadrantes
Potencias:          250-500 kW unitarios
Capacidad Q:        ±0.95 inductivo/capacitivo
Control:            Remoto SCADA
Funciones:          STATCOM, ramp control
Comunicación:       IEC 61850
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## ANÁLISIS COMPARATIVO DE IMPACTOS

### 1. Perfil de Tensión

#### Modelo Centralizado
```
Alimentador        Sin GD    Con GD Central   Mejora
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Industrial         0.94 pu   0.945 pu         +0.5%
Comercial          0.93 pu   0.935 pu         +0.5%
Turístico          0.91 pu   0.915 pu         +0.5%
Residencial        0.92 pu   0.925 pu         +0.5%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

#### Modelo Distribuido
```
Alimentador        Sin GD    Con GD Distrib.  Mejora
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Industrial         0.94 pu   0.962 pu         +2.2%
Comercial          0.93 pu   0.954 pu         +2.4%
Turístico          0.91 pu   0.941 pu         +3.1%
Residencial        0.92 pu   0.948 pu         +2.8%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 2. Pérdidas Técnicas

#### Análisis de Pérdidas I²R
```
REDUCCIÓN DE PÉRDIDAS POR MODELO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                 Base      Central.   Distrib.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pérdidas (MWh)   18,000    17,500     16,200
Reducción        -         500        1,800
Porcentaje       -         2.8%       10.0%
Valor anual      -         $37,500    $135,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Nota: El modelo distribuido reduce pérdidas localmente al acortar distancias entre generación y consumo.

### 3. Capacidad de Hosting

#### Límites de Penetración
```
CAPACIDAD DE HOSTING POR MODELO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Modelo          Actual    Futuro    Límite
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Centralizado    14.6 MW   14.6 MW   Rígido
Distribuido     14.5 MW   25+ MW    Flexible
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 4. Servicios Auxiliares

#### Compensación de Potencia Reactiva
```python
# Capacidad de compensación nocturna
Q_nocturno = {
    'Centralizado': 0,  # MVAr - Sin capacidad
    'Distribuido': {
        'Capacidad total': 11.2 * 0.33,  # 3.7 MVAr
        'Horas operación': 12,  # h/día
        'Factor utilización': 0.33,
        'Beneficio anual': 86_370  # USD/año
    }
}
```

### 5. Resiliencia y Confiabilidad

#### Análisis N-1
```
IMPACTO DE CONTINGENCIAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Evento              Central.        Distribuido
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Falla inversor      -20% gen.       -6% gen.
Falla línea MT      -100% gen.      -15% gen.
Mantenimiento       -100% gen.      -15% gen.
Evento climático    Alto impacto    Bajo impacto
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

#### Mejora en Índices
```
PROYECCIÓN DE ÍNDICES DE CALIDAD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Índice      Actual    Central.    Distribuido
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SAIDI       28.5 h    27.0 h      22.8 h
SAIFI       6.2       6.0         5.1
ENS         1,200 MWh 1,150 MWh   960 MWh
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## INTEGRACIÓN CON SISTEMA SCADA

### Arquitectura de Control
```
SISTEMA DE GESTIÓN DISTRIBUIDA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nivel 1: Centro de Control CEB
         ├── SCADA principal
         ├── Gestión de energía (EMS)
         └── Optimización en tiempo real

Nivel 2: Controladores de Campo
         ├── RTUs en cada punto GD
         ├── Medición sincrofasorial
         └── Control local inversores

Nivel 3: Inversores Inteligentes
         ├── Control P/Q independiente
         ├── Funciones grid support
         └── Protecciones integradas
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Funcionalidades Avanzadas
1. **Despacho óptimo**: Maximizar beneficios en tiempo real
2. **Control de tensión**: Coordinado multipunto
3. **Gestión de reactivo**: 24/7 optimizado
4. **Respuesta a contingencias**: Automática

## VENTAJAS TÉCNICAS DEL MODELO DISTRIBUIDO

### 1. Flexibilidad Operativa
- Reconfiguración ante contingencias
- Crecimiento modular
- Adaptación a cambios de demanda
- Múltiples modos de operación

### 2. Calidad de Energía
- Mejora de tensión localizada
- Reducción de flicker
- Compensación de armónicos
- Balance de fases

### 3. Eficiencia del Sistema
- Menores pérdidas totales
- Mejor factor de utilización
- Reducción de congestión
- Optimización de activos

### 4. Preparación para el Futuro
- Compatible con microrredes
- Integración de almacenamiento
- Vehicle-to-Grid ready
- Smart Grid habilitado

## CONCLUSIONES DEL ANÁLISIS TÉCNICO

El modelo distribuido multipropósito demuestra clara superioridad técnica sobre el centralizado:

1. **Mejora de tensión**: 5-6 veces superior
2. **Reducción de pérdidas**: 3.6 veces mayor
3. **Resiliencia**: Impacto de fallas 85% menor
4. **Servicios auxiliares**: USD 86,370/año adicionales
5. **Flexibilidad**: Crecimiento modular posible

La inversión adicional en sistemas de control e integración (incluida en el CAPEX) se justifica ampliamente por los beneficios técnicos obtenidos.

---

**Siguiente documento**: [03. Análisis Económico →](./03_analisis_economico.md)