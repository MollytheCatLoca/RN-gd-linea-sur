# 3. GENERACIÓN FOTOVOLTAICA ESPERADA

## 3.1 Parámetros de Generación

```
PARÁMETRO                    VALOR           FUENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Factor planta FV bifacial    18.4%           Análisis Fase 4
Horas sol equivalentes       4.42 h/día      1,613 h/año
Degradación anual           0.5%             Garantía fabricante
Disponibilidad              98%              Estándar industria
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 3.2 Generación Anual por Escenario (en MWh)

```
AÑO    ESCENARIO 1    ESCENARIO 2    ESCENARIO 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1      3,154          4,731          6,308
5      3,076          4,614          6,152
10     2,983          4,475          5,966
15     2,894          4,341          5,788
20     2,808          4,212          5,616
25     2,724          4,087          5,449
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 3.3 Balance Energético Local

```
CONCEPTO                 ESCENARIO 1    ESCENARIO 2    ESCENARIO 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Demanda local (MWh)      7,850          7,850          7,850
Generación FV (MWh)      3,154          4,731          6,308
Autoconsumo (MWh)        2,523          3,785          5,046
Inyección red (MWh)      631            946            1,262
% Autoabastecimiento     32.1%          48.2%          64.3%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 3.4 Operación en Isla - Capacidad y Autonomía

```
CONCEPTO                 ESCENARIO 1    ESCENARIO 2    ESCENARIO 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
BESS grid-forming        1.0 MW         1.5 MW         2.0 MW
Autonomía @ 0.9 MW       60 min         80 min         120 min
Autonomía @ 0.45 MW      120 min        160 min        240 min
Cobertura eventos        85%            99%            100%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Estrategia Operación Isla:
- **Día**: FV + BESS cubren demanda completa
- **Noche**: BESS mantiene cargas críticas (50% demanda)
- **Reconexión**: Sincronización suave con red principal

## 3.5 Servicio Q at Night - Compensación Reactiva

```
PARÁMETRO                ESCENARIO 1    ESCENARIO 2    ESCENARIO 3
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Capacidad inversores     2.0 MVA        3.0 MVA        4.0 MVA
Q disponible día         ±0.4 MVAr      ±0.6 MVAr      ±0.8 MVAr
Q disponible noche       ±2.0 MVAr      ±3.0 MVAr      ±4.0 MVAr
Horas operación Q/año    4,380          4,380          4,380
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Beneficios Q Nocturno:
- **Reducción pérdidas I²R**: 38.5% en horario nocturno
- **Mejora factor potencia**: 0.78 → 0.995
- **Ahorro energía**: 150 MWh/año
- **Estabilización voltaje**: ±2% variación máxima

## 3.6 Gestión Energética Integrada

### Prioridades de Operación:
1. **Emergencia/Reserva**: Respuesta instantánea ante contingencias
2. **Calidad de servicio**: Mantener V > 0.9 pu siempre
3. **Autoconsumo máximo**: Minimizar importación de red
4. **Q nocturno**: Compensación reactiva 24/7
5. **Arbitraje económico**: Cuando SOC > 80%

### Coordinación FV-BESS:
```
HORARIO          MODO OPERACIÓN                   PRIORIDAD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
06:00-09:00     FV rampa + BESS soporte          Estabilización
09:00-17:00     FV máximo + BESS carga           Autoconsumo
17:00-21:00     FV declive + BESS descarga       Soporte pico
21:00-06:00     BESS reserva + Q nocturno        Calidad/Reserva
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

🔹 **Notas importantes**:
- Los valores de generación consideran la degradación anual del 0.5% sobre 25 años
- El factor de planta 18.4% para bifaciales se basa en análisis detallado Fase 4
- La operación en isla requiere BESS con capacidad grid-forming
- El servicio Q at Night es fundamental para la estabilidad nocturna
- La gestión integrada maximiza beneficios técnicos y económicos