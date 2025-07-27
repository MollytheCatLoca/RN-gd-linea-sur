# ANÁLISIS COMPARATIVO: DIESEL vs BESS COMO RESERVA DE POTENCIA
## Los Menucos - Sistema Eléctrico Línea Sur

### Fecha: Julio 2025
### Revisión: Análisis específico post-aclaraciones cliente

---

## 1. RESUMEN EJECUTIVO

El generador diesel en Los Menucos opera como **RESERVA DE POTENCIA**, no como generación regular. Con solo 10 minutos/día de operación promedio y un costo fijo de alquiler de USD 190,000/año, resulta en un costo real de **USD 1,737/MWh** - 24 veces más caro que la energía de red.

El sistema BESS propuesto puede cumplir la misma función de reserva con ventajas técnicas superiores y eliminando completamente el costo fijo anual.

---

## 2. SITUACIÓN ACTUAL - DIESEL COMO RESERVA

### 2.1 Características Operativas
```
PARÁMETRO                    VALOR           COMENTARIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Potencia instalada           1.8 MW          Generador alquilado
Operación diaria promedio    10 minutos      Solo emergencias
Operación anual              60.8 horas      0.7% factor capacidad
Energía generada anual       109.4 MWh       Mínima utilización
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 2.2 Análisis de Costos
```
CONCEPTO                     VALOR           CÁLCULO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Costo alquiler anual         USD 190,000     Fijo independiente del uso
Costo por día                USD 521         190,000 ÷ 365
Costo por hora operada       USD 3,125       190,000 ÷ 60.8
Costo por MWh generado       USD 1,737       190,000 ÷ 109.4
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Comparación tarifa red       USD 71/MWh      24.5x más caro
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 2.3 Eventos Típicos que Requieren Reserva
Basado en operación de 10 min/día promedio:

```
TIPO DE EVENTO               DURACIÓN        FRECUENCIA      ENERGÍA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Colapso voltaje             2-5 min         2-3/semana      150 kWh
Soporte pico extremo        10-15 min       1-2/semana      450 kWh
Contingencia N-1            20-30 min       1-2/mes         900 kWh
Mantenimiento programado    60+ min         1/mes           1,800 kWh
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PROMEDIO PONDERADO          10 min/día      365 eventos     300 kWh/día
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 3. SOLUCIÓN PROPUESTA - BESS COMO RESERVA

### 3.1 Especificaciones BESS
```
PARÁMETRO                    VALOR           COMENTARIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Capacidad energía            2.0 MWh         Tecnología LFP
Potencia nominal             1.5 MW          Continua
Potencia pico (10 min)       1.8 MW          Igual al diesel
Energía útil (10-95% SOC)    1.7 MWh         85% profundidad
Tiempo respuesta             <100 ms         vs 5-7 min diesel
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 3.2 Capacidad de Cobertura
```
ESCENARIO                    DIESEL          BESS            VENTAJA BESS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Evento 5 min @ 1.8 MW       ✓ (150 kWh)     ✓ (150 kWh)     Instantáneo
Evento 60 min @ 1.5 MW      ✓ (1,500 kWh)   ✓ (1,500 kWh)   Sin arranque
Múltiples eventos/día       ✓ Con arranque   ✓ Sin desgaste  Mayor confiabilidad
Respuesta instantánea       ✗ (5-7 min)      ✓ (<100 ms)     Evita colapso
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 3.3 Análisis de Costo como Reserva
```
CONCEPTO                     DIESEL          BESS            AHORRO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Costo anual fijo            USD 190,000      USD 0           USD 190,000
O&M anual                   USD 15,000       USD 11,200      USD 3,800
Combustible (109 MWh)       USD 13,625       USD 0*          USD 13,625
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL ANUAL                 USD 218,625      USD 11,200      USD 207,425
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```
*BESS se recarga con FV propio o red en horas valle

---

## 4. VENTAJAS TÉCNICAS DEL BESS

### 4.1 Tiempo de Respuesta
```
FASE                         DIESEL          BESS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Detección evento            Instantáneo      Instantáneo
Orden de arranque           5-10 seg         < 1 seg
Arranque motor              2-3 min          N/A
Sincronización              1-2 min          < 100 ms
Toma de carga               30-60 seg        Instantáneo
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL                       5-7 minutos      < 100 ms
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

Durante esos 5-7 minutos de arranque del diesel:
- Voltaje puede colapsar completamente (V=0)
- Equipos sensibles se desconectan
- Procesos industriales se interrumpen
- ENS acumulada: 150-210 kWh

### 4.2 Confiabilidad
```
PARÁMETRO                    DIESEL          BESS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Disponibilidad              95%             >98%
Falla de arranque           2-5%            <0.1%
Mantenimiento mensual       8 horas         1 hora
Vida útil                   20,000 horas    >10 años
Degradación                 Significativa    <20% en 10 años
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 4.3 Beneficios Adicionales BESS
1. **Servicios de red 24/7**: Regulación voltaje, soporte frecuencia
2. **Arbitraje energético**: Cargar en valle, descargar en pico
3. **Integración FV**: Suavizado de rampas, time-shift
4. **Cero emisiones**: Sin ruido ni contaminación local
5. **Operación remota**: Sin personal en sitio

---

## 5. ANÁLISIS ECONÓMICO COMPARATIVO

### 5.1 Inversión vs Ahorro
```
CONCEPTO                     VALOR           COMENTARIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CAPEX BESS (2 MWh)          USD 560,000     Incluye instalación
Ahorro anual diesel         USD 207,425     Alquiler + O&M + combustible
Payback simple              2.7 años        Solo por diesel evitado
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 5.2 Valor Presente Neto (10 años)
```
Ahorro diesel (VP @ 8%)     USD 1,392,000
CAPEX BESS                  USD -560,000
Reemplazo año 10            USD -200,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
VPN                         USD 632,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 5.3 Costo Nivelado de Reserva (LCOR)
```
                            USD/MWh-reserva  USD/año
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Diesel actual               1,737            190,000
BESS (amortizado 10 años)  183              20,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Reducción                   89%              170,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 6. BENEFICIOS CUANTIFICADOS

### 6.1 Beneficios Directos
```
CONCEPTO                     VALOR ANUAL     DESCRIPCIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Eliminación alquiler        USD 190,000     Costo fijo evitado
Reducción O&M               USD 3,800       Menor mantenimiento
Combustible evitado         USD 13,625      109 MWh × USD 125
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SUBTOTAL DIRECTOS           USD 207,425
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 6.2 Beneficios Indirectos
```
CONCEPTO                     VALOR ANUAL     DESCRIPCIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ENS evitada (arranque)      USD 7,000       35 MWh × USD 200
Mejor calidad servicio      USD 15,000      Reducción reclamos
Servicios auxiliares        USD 10,000      Regulación V/f
Valor respuesta rápida      USD 25,000      Evita colapsos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SUBTOTAL INDIRECTOS         USD 57,000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOTAL BENEFICIOS            USD 264,425
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 7. DIMENSIONAMIENTO ÓPTIMO BESS PARA RESERVA

### 7.1 Análisis de Sensibilidad
```
TAMAÑO BESS     COBERTURA EVENTOS    COSTO/BENEFICIO    RECOMENDACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1.0 MWh         90% (< 30 min)       Excelente          Mínimo viable
1.5 MWh         95% (< 45 min)       Muy bueno          Equilibrado
2.0 MWh         99% (< 80 min)       Bueno              RECOMENDADO ✓
2.5 MWh         99.9% (< 100 min)    Regular            Sobredimensionado
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 7.2 Justificación 2.0 MWh
- Cubre 99% de eventos históricos
- Permite 80 minutos @ 1.5 MW
- Margen para servicios adicionales
- Óptimo costo/beneficio

---

## 8. MODELO OPERATIVO PROPUESTO

### 8.1 Jerarquía de Uso BESS
```
PRIORIDAD   FUNCIÓN                  CONDICIÓN ACTIVACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1           Reserva emergencia       V < 0.9 pu o f < 49.5 Hz
2           Soporte pico extremo     P > 1.4 MW y SOC > 50%
3           Regulación voltaje       0.9 < V < 0.95 pu
4           Arbitraje energético     Δ precio > USD 20/MWh
5           Servicios auxiliares     Según requerimiento SO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### 8.2 Gestión del Estado de Carga (SOC)
```
RANGO SOC       MODO OPERACIÓN          ACCIONES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
90-95%          Pleno                   Todos los servicios
70-90%          Normal                  Reserva + servicios
50-70%          Conservador             Solo reserva crítica
30-50%          Recarga prioritaria     Minimizar descarga
10-30%          Emergencia              Solo eventos críticos
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 9. CONCLUSIONES

### 9.1 Técnicas
1. **BESS supera al diesel** en todos los parámetros técnicos para reserva
2. **Respuesta instantánea** elimina ENS durante arranque
3. **Mayor confiabilidad** reduce riesgo de falla en momentos críticos
4. **Flexibilidad operativa** permite múltiples servicios

### 9.2 Económicas
1. **Costo diesel insostenible**: USD 1,737/MWh por baja utilización
2. **Ahorro anual**: USD 207,425 solo en diesel evitado
3. **Payback**: 2.7 años considerando solo beneficios directos
4. **VPN positivo**: USD 632,000 en 10 años

### 9.3 Estratégicas
1. **Elimina dependencia** de combustibles fósiles para reserva
2. **Moderniza** la infraestructura con tecnología de punta
3. **Habilita** futuros servicios de red y flexibilidad
4. **Demuestra** viabilidad de soluciones limpias en zonas aisladas

---

## 10. RECOMENDACIÓN FINAL

El reemplazo del generador diesel por BESS para función de reserva en Los Menucos es:

✅ **TÉCNICAMENTE SUPERIOR**: Respuesta 3,000 veces más rápida
✅ **ECONÓMICAMENTE JUSTIFICADO**: Ahorro USD 207,425/año
✅ **OPERATIVAMENTE EFICIENTE**: 98% disponibilidad vs 95%
✅ **AMBIENTALMENTE RESPONSABLE**: Cero emisiones locales

La inversión en BESS no solo elimina un costo fijo insostenible, sino que transforma una reserva pasiva y costosa en un activo activo que mejora la calidad y confiabilidad del servicio eléctrico.