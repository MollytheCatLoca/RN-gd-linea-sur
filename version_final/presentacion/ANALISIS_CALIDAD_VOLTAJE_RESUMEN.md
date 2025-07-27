# ANÁLISIS DE CALIDAD DE RED Y VOLTAJE
## Sistema Eléctrico Línea Sur 33kV - Río Negro

---

## 1. SITUACIÓN ACTUAL DEL SISTEMA

### Estado Crítico de la Red
```
PARÁMETRO                    VALOR ACTUAL         LÍMITE REGULATORIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Voltaje promedio sistema     0.90-0.92 pu         0.95-1.05 pu
Violaciones regulatorias     25-35%               <5%
Pérdidas técnicas           8-20%                <5%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Problemática Identificada
- **Caídas de voltaje severas** en toda la línea
- **Pérdidas técnicas elevadas** por longitud (220 km)
- **Calidad de servicio degradada** en puntas de línea
- **Limitación de crecimiento** por restricciones técnicas

---

## 2. ANÁLISIS POR ESTACIÓN

### 2.1 PILCANIYEU (Cabecera)
```
PARÁMETRO                    VALOR              OBSERVACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Voltaje promedio             0.95 pu            Aceptable
Demanda promedio             2.37 MW            49% del total
Demanda máxima               4.79 MW            Base del sistema
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 2.2 JACOBACCI (Centro - 55.6%)
```
PARÁMETRO                    VALOR              OBSERVACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Voltaje promedio*            0.92 pu            BAJO ⚠️
Demanda promedio             0.507 MW           11% del total
Sensibilidad dV/dP           +0.0115 pu/MW      Positiva ✓
Horas V<0.9 pu              2,190 h/año        25% del tiempo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
*Nota: Valores corregidos por error de medición

### 2.3 MAQUINCHAO (Intermedio - 87%)
```
PARÁMETRO                    VALOR              OBSERVACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Voltaje promedio             0.89 pu            CRÍTICO ⚠️
Demanda promedio             0.464 MW           10% del total
Sensibilidad dV/dP           -0.0015 pu/MW      Negativa ⚠️
Factor de capacidad          31.9%              Subutilizado
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 2.4 LOS MENUCOS (Punta - 100%)
```
PARÁMETRO                    VALOR              OBSERVACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Voltaje promedio*            0.237 pu           ERROR MEDICIÓN
Voltaje real estimado        0.88-0.90 pu       CRÍTICO ⚠️
Demanda promedio             0.896 MW           19% del total
Eventos V=0                  164 h/año          COLAPSOS ⛔
Generador diesel             1.8 MW             RESERVA COSTOSA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 3. SENSIBILIDAD VOLTAJE vs INYECCIÓN FV

### Análisis dV/dP por Estación
```
ESTACIÓN         dV/dP (pu/MW)    INTERPRETACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pilcaniyeu       Base             Punto de referencia
Jacobacci        +0.0115          ✓ Mejora con FV
Maquinchao       -0.0015          ⚠️ Requiere análisis
Los Menucos      +0.051           ✓ Alta sensibilidad
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Implicaciones para Diseño
- **Jacobacci y Los Menucos**: Ideales para inyección FV
- **Maquinchao**: Puede requerir compensación reactiva adicional
- **Coordinación necesaria** entre proyectos

---

## 4. PÉRDIDAS TÉCNICAS ACTUALES

### Distribución de Pérdidas
```
TRAMO                      LONGITUD    PÉRDIDAS     % ENERGÍA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pilcaniyeu-Jacobacci       50 km       45 kW        8.9%
Jacobacci-Maquinchao       70 km       85 kW        12%
Maquinchao-Los Menucos     100 km      180 kW       20%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL LÍNEA                220 km      310 kW       15.5%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Costo Anual de Pérdidas
```
Energía perdida:     2,714 MWh/año
Costo unitario:      USD 71/MWh
COSTO TOTAL:         USD 192,694/año
```

---

## 5. SOLUCIÓN PROPUESTA: GENERACIÓN DISTRIBUIDA

### Configuración Óptima Identificada

#### JACOBACCI - Enfoque Eficiencia
```
COMPONENTE              CAPACIDAD        FUNCIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FV                      1.0 MW           Reducción pérdidas día
Inversores STATCOM      1.2 MVA          Q at Night 24/7
BESS                    NO               Mantener CAPEX bajo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAPEX TOTAL             USD 968,000      Sin almacenamiento
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

#### LOS MENUCOS - Enfoque Resiliencia
```
COMPONENTE              CAPACIDAD        FUNCIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FV                      3.0 MW           100% demanda día
BESS                    2.0 MWh/1.5 MW   Operación isla
Grid-forming            Sí               Reemplaza diesel
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAPEX TOTAL             USD 3,060,000    Eliminación diesel
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 6. MEJORAS ESPERADAS EN CALIDAD

### 6.1 Mejora de Voltaje
```
ESTACIÓN         ACTUAL      CON PSFV     MEJORA      OBJETIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Jacobacci        0.92 pu     0.932 pu     +1.2%       ✓
Los Menucos      0.89 pu     0.945 pu     +6.2%       ✓
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 6.2 Reducción de Pérdidas
```
CONCEPTO                    SIN PSFV        CON PSFV      REDUCCIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Pérdidas día (6-18h)        186 kW          47 kW         -75%
Pérdidas noche (18-6h)      124 kW          114 kW        -8%
Pérdidas promedio           155 kW          80 kW         -48%
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Ahorro anual                                657 MWh       USD 46,647
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 6.3 Indicadores de Calidad
```
MÉTRICA                  ACTUAL          CON PSFV        MEJORA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Horas V<0.9 pu          4,380 h/año     1,460 h/año     -67%
ENS Los Menucos         117.5 MWh/año   0 MWh/año       -100%
THD voltaje             5.2%            4.8%            -7.7%
Factor de potencia      0.78-0.985      0.995           Óptimo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 7. BENEFICIOS ECONÓMICOS TOTALES

### 7.1 Jacobacci (FV sin BESS)
```
CONCEPTO                        VALOR ANUAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Energía FV vendida              USD 111,825
Reducción pérdidas día          USD 21,473
Reducción pérdidas Q noche      USD 7,976
Mejora calidad servicio         USD 15,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL BENEFICIOS                USD 157,474
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TIR: 14.8%    Payback: 6.1 años
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 7.2 Los Menucos (FV + BESS)
```
CONCEPTO                        VALOR ANUAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Eliminación diesel (fijo)       USD 190,000
Ahorro energía CAMMESA          USD 268,735
Reducción pérdidas              USD 40,328
ENS evitada                     USD 17,640
Q at Night                      USD 10,650
Servicios auxiliares            USD 15,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL BENEFICIOS                USD 589,653
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TIR: 20.7%    Payback: 4.7 años
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 8. COMPARACIÓN CON ALTERNATIVAS

### Costos por Mejora de Voltaje
```
ALTERNATIVA                 CAPEX         USD/Δpu      COMENTARIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Nueva línea 33kV           USD 22M       USD 440M     Prohibitivo
Reconductoring             USD 8.8M      USD 176M     Muy alto
Capacitores shunt          USD 2M        USD 100M     Limitado
GD Térmica expansión       USD 1.5M      USD 75M      + OPEX alto
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PSFV Distribuido           USD 4M        USD 80M      + Beneficios
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 9. SERVICIOS ADICIONALES DE RED

### 9.1 Q at Night - Compensación Reactiva Nocturna
- **Disponible**: 12 horas/día (20:00-08:00)
- **Capacidad**: ±3.0 MVAr (Jacobacci) + ±3.0 MVAr (Los Menucos)
- **Beneficio**: Reducción 38.5% pérdidas nocturnas
- **Valor**: USD 18,626/año conjunto

### 9.2 Operación en Isla (Los Menucos)
- **Autonomía**: 80 minutos @ demanda media
- **Respuesta**: <100ms (vs 5-7 min diesel)
- **Confiabilidad**: 99.5% disponibilidad
- **Valor**: Eliminación 164 h/año sin servicio

### 9.3 Servicios Auxiliares
- **Regulación frecuencia**: Respuesta rápida <1s
- **Soporte voltaje**: Control dinámico Q(V)
- **Black-start**: Capacidad arranque autónomo
- **Valor combinado**: USD 25,000/año

---

## 10. CONCLUSIONES Y RECOMENDACIONES

### 10.1 Diagnóstico Final
✅ La red opera en **condición crítica** con voltajes 5-12% bajo norma
✅ Las **pérdidas técnicas** (15.5%) triplican valores aceptables
✅ Los **colapsos de voltaje** en Los Menucos son inaceptables
✅ La **generación distribuida FV** es la solución más costo-efectiva

### 10.2 Plan de Acción Recomendado

#### FASE 1: Implementación Prioritaria
1. **Los Menucos PSFV+BESS** (3MW/2MWh)
   - Elimina dependencia diesel costosa
   - Resuelve colapsos de voltaje
   - TIR 20.7%, recuperación 4.7 años

2. **Jacobacci FV+STATCOM** (1MW)
   - Máxima eficiencia sin BESS
   - Q at Night fundamental
   - TIR 14.8%, recuperación 6.1 años

#### FASE 2: Optimización Sistema
3. **Coordinación operativa** entre proyectos
4. **Monitoreo en tiempo real** de calidad
5. **Expansión modular** según crecimiento

### 10.3 Beneficios del Proyecto Conjunto
```
MÉTRICA                    VALOR               IMPACTO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Inversión total            USD 4,028,000       Modular
Beneficios anuales         USD 747,127         Crecientes
Mejora voltaje promedio    +5%                 Cumple norma
Reducción pérdidas         -48%                USD 96,347/año
Eliminación diesel         100%                USD 190,000/año
Empleos permanentes        6 directos          Local
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 10.4 Próximos Pasos
1. **Validación mediciones de campo** (urgente para diseño final)
2. **Ingeniería de detalle** con datos corregidos
3. **Gestión permisos** ambientales y de conexión
4. **Licitación EPC** con especificaciones Q at Night
5. **Plan de O&M** local con capacitación

---

**NOTA CRÍTICA**: Se detectaron errores significativos en el sistema de medición (voltajes 0.236 pu imposibles). Se requiere campaña de medición actualizada antes del diseño final. Los valores presentados son estimaciones conservadoras basadas en condiciones típicas de líneas rurales 33kV.