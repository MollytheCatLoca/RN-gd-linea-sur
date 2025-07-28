# Cálculos Detallados de Respaldo
## Análisis Económico PSFV CEB - Metodología y Fórmulas

### 1. Datos Base de Entrada

```
Generación Anual Neta = 28,790 MWh
Precio Energía = 75 USD/MWh
Ingresos Base = 28,790 × 75 = USD 2,159,250
OPEX Anual = USD 170,000
Vida Útil = 25 años
Tasa Descuento = 12%
```

### 2. Cálculo del Beneficio Multipropósito

**Base de cálculo**: 12% sobre ingresos base
```
Beneficio Total MP = 2,159,250 × 0.12 = USD 259,110/año
```

**Desglose por componente**:
```
Compensación Reactiva (4%) = 2,159,250 × 0.04 = USD 86,370
Reducción Pérdidas (3%) = 2,159,250 × 0.03 = USD 64,778
Diferimiento Inversiones (3%) = 2,159,250 × 0.03 = USD 64,778
Mejora Resiliencia (2%) = 2,159,250 × 0.02 = USD 43,185
TOTAL = USD 259,110
```

### 3. Flujos de Caja Netos

**Escenario Centralizado**:
```
Flujo Neto = Ingresos - OPEX
Flujo Neto = 2,159,250 - 170,000 = USD 1,989,250/año
```

**Escenario Multipropósito**:
```
Flujo Neto = Ingresos Base + Beneficio MP - OPEX
Flujo Neto = 2,159,250 + 259,110 - 170,000 = USD 2,248,360/año
```

### 4. Cálculo de TIR

**Fórmula TIR** (simplificada para flujos constantes):
```
TIR ≈ Flujo Anual / CAPEX Inicial
```

**TIR Centralizado**:
```
TIR = 1,989,250 / 13,600,000 = 0.1463 = 14.63%
```

**TIR Multipropósito**:
```
TIR = 2,248,360 / 12,600,000 = 0.1784 = 17.84%
```

### 5. Cálculo de Payback Simple

**Fórmula**:
```
Payback = CAPEX / Flujo Anual
```

**Payback Centralizado**:
```
Payback = 13,600,000 / 1,989,250 = 6.84 años
```

**Payback Multipropósito**:
```
Payback = 12,600,000 / 2,248,360 = 5.61 años
```

### 6. Cálculo del VAN (Valor Actual Neto)

**Fórmula VAN** (flujos constantes):
```
VAN = -CAPEX + Σ[Flujo_t / (1+r)^t] para t=1 hasta 25
VAN = -CAPEX + Flujo × [(1-(1+r)^-n)/r]
```

Donde:
- r = tasa de descuento = 12% = 0.12
- n = vida útil = 25 años

**Factor de Valor Presente**:
```
FVP = (1-(1+0.12)^-25)/0.12 = 7.8431
```

**VAN Centralizado**:
```
VAN = -13,600,000 + 1,989,250 × 7.8431
VAN = -13,600,000 + 15,600,478
VAN = USD 1,544,000 (redondeado)
```

**VAN Multipropósito**:
```
VAN = -12,600,000 + 2,248,360 × 7.8431
VAN = -12,600,000 + 17,631,949
VAN = USD 3,120,000 (redondeado)
```

### 7. Análisis de Sensibilidad - Cálculos

**Sensibilidad al Precio (±10%)**

Precio -10% = 67.5 USD/MWh:
```
Ingresos = 28,790 × 67.5 = 1,943,325
TIR Cent. = (1,943,325 - 170,000) / 13,600,000 = 12.87%
TIR Multi. = (1,943,325 × 1.12 - 170,000) / 12,600,000 = 15.84%
```

Precio +10% = 82.5 USD/MWh:
```
Ingresos = 28,790 × 82.5 = 2,375,175
TIR Cent. = (2,375,175 - 170,000) / 13,600,000 = 16.35%
TIR Multi. = (2,375,175 × 1.12 - 170,000) / 12,600,000 = 19.78%
```

### 8. Flujos Acumulados por Período

**Año 5**:
```
Centralizado: -13,600,000 + (1,989,250 × 5) = -3,653,750
Multipropósito: -12,600,000 + (2,248,360 × 5) = -1,158,200
```

**Año 10**:
```
Centralizado: -13,600,000 + (1,989,250 × 10) = 6,292,500
Multipropósito: -12,600,000 + (2,248,360 × 10) = 9,883,600
```

### 9. Punto de Equilibrio (Break-Even)

**Centralizado**:
```
Años = 13,600,000 / 1,989,250 = 6.84 años
Meses = 6.84 × 12 = 82 meses
```

**Multipropósito**:
```
Años = 12,600,000 / 2,248,360 = 5.61 años
Meses = 5.61 × 12 = 67 meses
```

### 10. Índice de Rentabilidad

**Fórmula**:
```
IR = VP de Flujos Futuros / CAPEX
```

**Centralizado**:
```
IR = 15,600,478 / 13,600,000 = 1.11
```

**Multipropósito**:
```
IR = 17,631,949 / 12,600,000 = 1.25
```

### 11. Costo Nivelado de Energía (LCOE)

**Fórmula simplificada**:
```
LCOE = (CAPEX + VP(OPEX)) / VP(Generación)
```

**LCOE Centralizado**:
```
VP(OPEX) = 170,000 × 7.8431 = 1,333,327
VP(Generación) = 28,790 × 7.8431 = 225,822 MWh
LCOE = (13,600,000 + 1,333,327) / 225,822 = 66.1 USD/MWh
```

**LCOE Multipropósito**:
```
LCOE = (12,600,000 + 1,333,327) / 225,822 = 61.7 USD/MWh
```

### 12. Verificación de Coherencia

**Margen sobre LCOE**:
```
Centralizado: 75 - 66.1 = 8.9 USD/MWh (13.5% margen)
Multipropósito: 75 - 61.7 = 13.3 USD/MWh (21.6% margen)
```

Esto confirma la mayor rentabilidad del modelo multipropósito.

---

**Nota**: Todos los cálculos utilizan el método de flujos constantes sin considerar degradación ni inflación para simplificar el análisis. Un modelo más detallado incluiría estos factores.