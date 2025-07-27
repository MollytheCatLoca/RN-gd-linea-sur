# 💲 2. ESCENARIOS DE INVERSIÓN

## 2.1 Configuraciones Propuestas

```
ESCENARIO    FV(MW)    BESS(MWh/MW)    CAPEX FV     CAPEX BESS    CAPEX TOTAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1            2.0       1.5/1.0          1,400,000    420,000       1,820,000
2            3.0       2.0/1.5          2,100,000    560,000       2,660,000
3            4.0       3.0/2.0          2,800,000    840,000       3,640,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 2.2 Capacidades Técnicas por Escenario

### Escenario 1: Conservador
```
FUNCIÓN                      CAPACIDAD              COBERTURA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generación FV diurna         2.0 MW                 70% demanda día
Almacenamiento               1.5 MWh                60 min @ 1.0 MW
Reserva de potencia          1.0 MW continuo        Parcial diesel
Operación isla               45 min @ demanda crítica
Q at Night                   ±2.0 MVAr              FP 0.78→0.95
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Escenario 2: Recomendado ⭐
```
FUNCIÓN                      CAPACIDAD              COBERTURA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generación FV diurna         3.0 MW                 100% demanda día
Almacenamiento               2.0 MWh                80 min @ 1.5 MW
Reserva de potencia          1.5 MW continuo        100% reemplazo diesel
Operación isla               80 min @ demanda media
Q at Night                   ±3.0 MVAr              FP 0.78→0.995
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Escenario 3: Agresivo
```
FUNCIÓN                      CAPACIDAD              COBERTURA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generación FV diurna         4.0 MW                 130% demanda día
Almacenamiento               3.0 MWh                120 min @ 2.0 MW
Reserva de potencia          2.0 MW continuo        Excede diesel actual
Operación isla               3+ horas autonomía
Q at Night                   ±4.0 MVAr              FP 0.78→0.999
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 2.2 Desglose de Inversión (USD)

```
COMPONENTE           ESCENARIO 1    ESCENARIO 2    ESCENARIO 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Módulos FV           700,000        1,050,000      1,400,000
Inversores           280,000        420,000        560,000
Estructura           210,000        315,000        420,000
Instalación DC       210,000        315,000        420,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Subtotal FV          1,400,000      2,100,000      2,800,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BESS                 300,000        400,000        600,000
BMS & Control        60,000         80,000         120,000
Instalación AC       60,000         80,000         120,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Subtotal BESS        420,000        560,000        840,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ingeniería (5%)      91,000         133,000        182,000
Contingencia (10%)   182,000        267,000        364,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL CAPEX          2,093,000      3,060,000      4,186,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 2.3 Análisis Comparativo de Beneficios

```
BENEFICIO                    ESCENARIO 1    ESCENARIO 2    ESCENARIO 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Eliminación diesel           Parcial        100% ✓         100% ✓
Ahorro anual (USD)          425,000        708,445        850,000
Mejora voltaje              12%            15%            18%
Autonomía isla              Limitada       Adecuada       Extendida
Flexibilidad futura         Baja           Alta           Muy Alta
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 2.4 Métricas Financieras por Escenario

```
MÉTRICA              ESCENARIO 1    ESCENARIO 2    ESCENARIO 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAPEX (USD)          2,093,000      3,060,000      4,186,000
TIR (%)              20.3%          18.5%          16.2%
VAN @ 12% (USD)      1,856,234      2,458,789      2,834,567
Payback (años)       4.5            5.2            5.9
LCOE (USD/MWh)       38.1           42.3           48.7
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 2.5 Justificación Escenario 2

✅ **Elimina completamente** el costo fijo del diesel (USD 190,000/año)
✅ **Cubre 100%** de eventos de reserva históricos
✅ **Proporciona** 80 minutos de autonomía en isla
✅ **Optimiza** inversión vs beneficios (TIR 18.5%)
✅ **Permite** expansión futura modular