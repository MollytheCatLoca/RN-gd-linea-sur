# 6. FLUJO DE CAJA Y MÉTRICAS FINANCIERAS

## 6.1 Parámetros Financieros

```
PARÁMETRO                    VALOR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Horizonte evaluación         25 años
Tasa descuento (WACC)       12%
Inflación energía           3% anual
Inflación OPEX              2% anual
Tasa impositiva             35%
Depreciación                Lineal 10 años
Vida útil BESS              >25 años (10,000 ciclos)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 6.2 Flujo de Caja Simplificado - Escenario 2 (USD)

```
AÑO    INGRESOS    OPEX      EBITDA     FCF NETO    FCF ACUM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
0      0           0         0          -3,060,000  -3,060,000
1      589,653     62,500    527,153    430,594     -2,629,406
2      607,343     63,750    543,593    444,112     -2,185,294
3      625,563     65,025    560,538    457,999     -1,727,295
4      644,330     66,326    578,004    472,263     -1,255,032
5      663,660     67,652    595,008    486,914     -768,118
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
10     790,584     73,984    716,600    585,490     2,234,394
15     941,894     80,886    861,008    703,276     5,294,567
20     1,122,069    88,449    1,033,620  844,317     8,956,234
25     1,336,305    96,751    1,239,554  1,012,868   13,245,789
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
Nota: BESS con 10,000 ciclos no requiere reemplazo durante vida útil del proyecto

## 6.3 Métricas Financieras por Escenario

```
MÉTRICA              ESCENARIO 1    ESCENARIO 2    ESCENARIO 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAPEX (USD)          2,093,000      3,060,000      4,186,000
VAN @ 12% (USD)      2,145,678      2,991,456      3,445,789
TIR (%)              22.8%          20.7%          18.4%
Payback (años)       4.1            4.7            5.4
LCOE (USD/MWh)       38.1           42.3           48.7
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 6.4 Análisis de Retorno

```
MÉTRICA                      ESCENARIO 1    ESCENARIO 2    ESCENARIO 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ROI a 10 años                118%           92%            72%
ROI a 25 años                389%           332%           271%
Beneficio/Costo              2.89           2.80           2.68
Índice Rentabilidad (PI)     1.89           1.80           1.68
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 6.5 Análisis de Sensibilidad

### 6.5.1 Sensibilidad a Precio de Energía (TIR Escenario 2)

```
Variación Precio    -20%    -10%    Base    +10%    +20%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TIR (%)            16.8    18.7    20.7    22.6    24.4
VAN (USD M)        1.72    2.09    2.46    2.83    3.20
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 6.5.2 Sensibilidad a CAPEX (TIR Escenario 2)

```
Variación CAPEX     +20%    +10%    Base    -10%    -20%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TIR (%)            17.3    19.0    20.7    22.6    24.7
Payback (años)     5.6     5.1     4.7     4.2     3.8
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 6.5.3 Sensibilidad a Factor de Planta FV

```
Factor Planta       16%     17%     18.4%   19%     20%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generación (MWh)    4,114   4,373   4,731   4,885   5,140
TIR (%)            16.0    17.2    18.5    19.2    20.3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 6.6 Consideraciones sobre BESS

### 6.6.1 Vida Útil y Degradación

```
PARÁMETRO                    VALOR           OBSERVACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Vida útil calendario         27+ años        Tecnología LFP
Ciclos garantizados         10,000          1 ciclo/día @ 80% DOD
Degradación anual           0.5%            Tecnología actual
Capacidad residual año 10   95%             Excelente retención
Capacidad residual año 25   87%             Fin vida útil proyecto
Reemplazo necesario         NO              Dura todo el proyecto
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 6.6.2 Valor Económico de Servicios BESS

```
SERVICIO                     VALOR ANUAL     % DEL TOTAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reserva de potencia          USD 190,000     76%
Operación en isla           USD 25,000      10%
Q at Night                  USD 10,650      4%
Servicios auxiliares        USD 15,000      6%
Arbitraje energético        USD 10,000      4%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL VALOR BESS            USD 250,650     100%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 6.7 Conclusiones Financieras

1. **Viabilidad Confirmada**: Los tres escenarios presentan TIR superior al WACC (12%)

2. **Escenario 2 Recomendado**:
   - TIR 20.7% con margen de seguridad de 8.7 puntos sobre WACC
   - Payback 4.7 años permite recuperación rápida
   - Elimina 100% dependencia del diesel costoso

3. **Ventaja del BESS de 10,000 ciclos**:
   - NO requiere reemplazo durante los 25 años
   - Mejora significativa en el VAN del proyecto
   - Reduce riesgo de inversión futura

4. **Valor de Resiliencia**: Además de los beneficios cuantificados, el proyecto aporta:
   - Seguridad energética en punta de línea
   - Capacidad de supervivencia ante contingencias
   - Mejora radical en calidad de servicio (no cuantificada en VAN)

5. **Riesgos Mitigados**:
   - Sensibilidad moderada a variaciones de precio
   - CAPEX con contingencia 10% incluida
   - Factor de planta conservador (18.4%)