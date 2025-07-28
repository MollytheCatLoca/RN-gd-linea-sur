# 1. INTRODUCCIÓN

## 1.1 Contexto y Motivación

La Cooperativa Eléctrica Bariloche (CEB) opera una red de distribución eléctrica que abastece a más de 68,500 usuarios en San Carlos de Bariloche y zonas aledañas, enfrentando desafíos característicos de un sistema en expansión con infraestructura heredada. Los factores críticos que definen el contexto operativo incluyen el incremento sostenido de la demanda impulsado por el crecimiento poblacional y turístico, la extensión geográfica del área de servicio que abarca zonas de compleja topografía, y las condiciones climáticas adversas propias de la región patagónica.

Esta combinación de factores ha derivado en índices de calidad de servicio que requieren atención prioritaria. Los indicadores SAIDI (System Average Interruption Duration Index) y SAIFI (System Average Interruption Frequency Index) revelan zonas críticas con interrupciones que impactan significativamente tanto a usuarios residenciales como a sectores productivos clave, particularmente el turismo y la industria local.

En este contexto, la generación distribuida emerge no solo como una alternativa para incrementar la capacidad del sistema, sino como una oportunidad transformadora para reimaginar la arquitectura de la red eléctrica. La evolución tecnológica de los sistemas fotovoltaicos, combinada con avances en electrónica de potencia y sistemas de control inteligente, permite concebir soluciones que trascienden el paradigma tradicional de generación centralizada.

## 1.2 Objetivos del Estudio

### Objetivo Principal

Evaluar el potencial técnico-económico de implementar un sistema de generación solar fotovoltaica distribuida bajo un enfoque multipropósito, que maximice la creación de valor mediante la captura sinérgica de beneficios operativos, económicos y de confiabilidad en la red de distribución de la CEB.

### Objetivos Específicos

1. **Caracterizar la topología actual de la red** mediante técnicas avanzadas de análisis de sistemas eléctricos, identificando los nodos críticos donde la inyección de generación distribuida tendría el mayor impacto positivo en la operación del sistema.

2. **Identificar y cuantificar oportunidades de valor** más allá de la simple generación de energía, incluyendo la reducción de pérdidas técnicas, la compensación de potencia reactiva, el diferimiento de inversiones en infraestructura y la mejora en los índices de confiabilidad.

3. **Diseñar una estrategia de implementación** que optimice la ubicación y dimensionamiento de los recursos de generación distribuida, considerando las restricciones técnicas, económicas y regulatorias del sistema.

4. **Desarrollar un marco metodológico replicable** que permita a otras cooperativas eléctricas evaluar y capturar los beneficios del enfoque multipropósito en sus propios sistemas de distribución.

5. **Establecer una hoja de ruta** para la modernización progresiva del sistema eléctrico, alineada con las tendencias globales hacia redes inteligentes y sistemas de energía descentralizados.

## 1.3 Marco Conceptual del Enfoque Multipropósito

### 1.3.1 Optimización de Puntos de Inyección

La ubicación estratégica de recursos de generación distribuida representa un cambio paradigmático respecto al enfoque tradicional de parques solares centralizados. La teoría de flujos óptimos de potencia establece que la minimización de las distancias eléctricas entre generación y carga reduce significativamente las pérdidas del sistema y mejora los perfiles de tensión.

Desde una perspectiva de inversión en infraestructura, la distribución inteligente de la capacidad de generación permite aprovechar la infraestructura existente de media tensión, reduciendo sustancialmente los costos de interconexión. Mientras que un parque centralizado requiere típicamente nuevas líneas de transmisión y subestaciones dedicadas, la generación distribuida puede conectarse en puntos existentes de la red, como subestaciones de distribución o centros de transformación estratégicamente ubicados.

### 1.3.2 Reducción de Pérdidas Técnicas

Las pérdidas técnicas en sistemas de distribución, gobernadas por la ley de Joule (P = I²R), representan un costo operativo significativo y una ineficiencia sistémica. La generación distribuida modifica fundamentalmente los patrones de flujo de potencia en la red, reduciendo las corrientes que circulan por los alimentadores principales al satisfacer parte de la demanda localmente.

Este fenómeno es particularmente relevante en sistemas con alimentadores extensos, donde las pérdidas pueden alcanzar valores significativos. La inyección de potencia cerca de los centros de carga no solo reduce las pérdidas óhmicas, sino que también mejora la regulación de tensión, permitiendo operar el sistema dentro de límites más estrechos y eficientes.

### 1.3.3 Compensación de Potencia Reactiva mediante Inversores Inteligentes

Los inversores modernos empleados en sistemas fotovoltaicos han evolucionado más allá de su función básica de conversión DC/AC. Estos dispositivos, equipados con electrónica de potencia avanzada, pueden operar como compensadores estáticos de potencia reactiva (STATCOMs distribuidos), proporcionando o absorbiendo potencia reactiva según las necesidades del sistema.

Durante las horas nocturnas, cuando la generación fotovoltaica es nula, estos inversores pueden continuar operando exclusivamente como compensadores de reactivo, mejorando el factor de potencia del sistema. Esta funcionalidad es particularmente valiosa en redes de distribución con cargas inductivas significativas, donde las penalizaciones por bajo factor de potencia representan un costo operativo considerable.

La capacidad de control de potencia reactiva también contribuye a la estabilidad de tensión, permitiendo un control más fino y distribuido que el obtenido con bancos de capacitores tradicionales. Además, la respuesta dinámica de los inversores electrónicos supera ampliamente a los dispositivos de compensación convencionales.

### 1.3.4 Creación de Valor Sinérgico

El concepto de "value stacking" o apilamiento de valor es fundamental para comprender la superioridad económica del enfoque multipropósito. A diferencia de un proyecto de generación tradicional que monetiza únicamente la energía producida, el modelo distribuido multipropósito captura valor en múltiples dimensiones simultáneamente:

- **Valor energético**: Generación de energía limpia desplazando fuentes más costosas
- **Valor de red**: Reducción de pérdidas y mejora de calidad de servicio
- **Valor de capacidad**: Diferimiento de inversiones en infraestructura
- **Valor de resiliencia**: Mejora en la confiabilidad mediante redundancia distribuida
- **Valor ambiental**: Reducción de emisiones y cumplimiento de objetivos de sostenibilidad

Esta aproximación representa una transición de las economías de escala tradicionales hacia las economías de alcance, donde el valor se maximiza no por el tamaño de la instalación, sino por la diversidad de servicios que puede proporcionar al sistema.

## 1.4 Metodología

El desarrollo del estudio sigue un enfoque metodológico que combina técnicas tradicionales de ingeniería eléctrica con herramientas avanzadas de ciencia de datos y optimización:

### Auditoría de Red y Análisis Topológico
Relevamiento exhaustivo de la infraestructura existente, incluyendo la caracterización de alimentadores, subestaciones, centros de transformación y puntos críticos de la red. Este análisis establece la línea base para la evaluación de mejoras.

### Análisis de Datos Históricos con Machine Learning
Procesamiento de grandes volúmenes de datos operativos, incluyendo registros de interrupciones, mediciones de calidad de energía, perfiles de demanda y reclamos de usuarios. La aplicación de algoritmos de aprendizaje automático permite identificar patrones no evidentes y correlaciones complejas entre variables del sistema.

### Optimización mediante Teoría de Grafos
La red eléctrica se modela como un grafo ponderado, donde los nodos representan puntos de conexión y las aristas los elementos de red. Algoritmos de optimización determinan las ubicaciones óptimas para la inyección de generación distribuida, considerando múltiples objetivos y restricciones.

### Simulación de Escenarios Comparativos
Desarrollo de modelos detallados que permiten comparar el desempeño del sistema bajo diferentes configuraciones: escenario base sin generación distribuida, escenario con generación centralizada tradicional, y escenario con generación distribuida multipropósito.

### Validación Técnico-Económica
Evaluación integral que considera no solo los aspectos técnicos, sino también la viabilidad económica, el marco regulatorio aplicable, y los impactos socioambientales del proyecto.

Esta metodología integral permite capturar la complejidad del sistema eléctrico y evaluar de manera rigurosa los beneficios del enfoque multipropósito, estableciendo una base sólida para la toma de decisiones informadas sobre la modernización de la infraestructura eléctrica de la CEB.