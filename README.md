# DAC mediante PWM con Arduino

## Implementación de Conversor Digital-Analógico usando Modulación PWM

![Arduino](https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

---

## Resumen

Este proyecto implementa un convertidor digital-analógico (DAC) mediante modulación por ancho de pulso (PWM) en plataforma Arduino. El sistema permite generar señales analógicas complejas (senoidal, triangular, cuadrada y sierra) a partir de datos digitales almacenados en tablas de búsqueda (LUT).

**Características principales:**
- Frecuencia de salida: 3.006 Hz
- Resolución: 8 bits efectivos  
- 4 formas de onda disponibles
- Control interactivo mediante pulsador

---

## Objetivos

### Objetivo General
Implementar y analizar un convertidor digital-analógico basado en modulación PWM capaz de generar múltiples formas de onda analógicas.

### Objetivos Específicos
- Diseñar tablas de búsqueda (LUT) para cuatro formas de onda características
- Implementar modulación PWM de alta frecuencia para minimizar componentes espectrales no deseadas
- Evaluar la resolución y linealidad del DAC implementado
- Analizar las características espectrales y de ruido del sistema

---

## Fundamentos Teóricos

### Principios de Conversión DAC por PWM

La modulación por ancho de pulso (PWM) permite generar señales analógicas mediante la variación del ciclo de trabajo (duty cycle) de una señal digital de frecuencia fija.

```
V_out = V_cc × (D/255)
```

**Donde:**
- `V_out`: Tensión de salida analógica
- `V_cc`: Tensión de alimentación (5V)  
- `D`: Valor digital (0-255 para 8 bits)

### Timer1 ATmega328P

Configuración en modo Fast PWM de 8 bits:

| Parámetro | Fórmula | Valor |
|-----------|---------|-------|
| Frecuencia PWM | `F_cpu / (Prescaler × 256)` | 62.5 kHz |
| Prescaler | - | 1 |
| Resolución | - | 8 bits (256 niveles) |

---

## Arquitectura del Sistema

```
[Tablas LUT] → [Selector de Forma] → [PWM Generator] → [Pin 9] → [Filtro RC] → [Señal Analógica]
     ↑                  ↑
[Programa]         [Botón Pin 2]
```

---

## Configuración del Hardware

### Componentes Principales

| Componente | Especificación |
|------------|----------------|
| **Microcontrolador** | ATmega328P (Arduino Uno) |
| **Pin PWM** | Pin 9 (OC1A) |
| **Control** | Pin 2 (pulsador con pull-up interno) |
| **Comunicación** | UART a 115200 bps |

### Configuración del Timer1

```cpp
TCCR1B = (TCCR1B & 0b11111000) | 0x01; // Prescaler = 1
```

---

## Estructura de Datos

### Tablas de Búsqueda (LUT)

```cpp
const uint8_t onda_senoidal[256] = { /* valores pre-calculados */ };
```

**Características:**
- Resolución angular: 360°/256 = 1.40625° por muestra
- Precisión temporal: 1/256 del período de la señal
- Eficiencia de memoria: 256 bytes por forma de onda

### Algoritmo de Generación

```cpp
for (int i = 0; i < N; i++) {
    uint8_t valor = tabla_seleccionada[i];
    analogWrite(pinPWM, valor);
    delayMicroseconds(delay_us);
}
```

**Análisis temporal:**
- Período por muestra: 1300 µs
- Período total: 256 × 1300 µs = 332.8 ms
- Frecuencia de salida: 1/0.3328s ≈ 3.006 Hz

---

## Especificaciones Técnicas

| Parámetro | Valor | Unidad |
|-----------|-------|--------|
| **Resolución** | 8 | bits |
| **Frecuencia PWM** | 62.5 | kHz |
| **Frecuencia de salida** | 3.006 | Hz |
| **Tensión de salida máxima** | 5.0 | V |
| **Impedancia de salida** | < 50 | Ω |
| **Linealidad integral (INL)** | ±0.5 | LSB |
| **Tiempo de establecimiento** | < 16 | µs |

---

## Validación Experimental

### Metodología de Pruebas

**Sistema de medición:**
- ADC: MCP3208 (12 bits, 8 canales)
- Frecuencia de muestreo: 200 Hz
- Resolución: 4096 niveles (0-5V)

### Resultados Experimentales

**Mediciones realizadas:**
1. Linealidad del DAC
2. Respuesta en frecuencia
3. Distorsión armónica
4. Estabilidad temporal

### Comparación con Especificaciones

| Parámetro | Especificado | Medido | Desviación |
|-----------|--------------|--------|------------|
| **Frecuencia de salida** | 3.006 Hz | 3.0 Hz | -0.2% |
| **Amplitud máxima** | 5.0 V | 4.95 V | -1% |
| **Linealidad** | ±0.5 LSB | ±0.8 LSB | +60% |

---

## Aplicaciones y Casos de Uso

### Aplicaciones Inmediatas

1. **Generación de señales de prueba** para sistemas analógicos
2. **Control de actuadores analógicos** (motores, válvulas)
3. **Síntesis de audio simple** (baja fidelidad)
4. **Simulación de sensores analógicos**

### Limitaciones

- No apto para audio de alta fidelidad (THD > -40 dB)
- Frecuencias limitadas (< 10 Hz prácticamente)
- Requiere filtrado externo para la mayoría de aplicaciones

---

## Análisis Económico

### Costo de Implementación

| Componente | Cantidad | Costo Unitario (Bs.) | Costo Total (Bs.) |
|------------|----------|---------------------|-------------------|
| Arduino Uno | 1 | 85.00 | 85.00 |
| Resistencias | 2 | 0.20 | 0.40 |
| Capacitores | 1 | 1.00 | 1.00 |
| Pulsador | 1 | 1.50 | 1.50 |
| **TOTAL** | - | - | **87.90** |

---

## Conclusiones

### Logros Alcanzados

1. **Implementación exitosa** de un DAC basado en PWM con resolución de 8 bits
2. **Generación de múltiples formas de onda** mediante tablas de búsqueda optimizadas
3. **Sistema de control interactivo** con selección de formas de onda
4. **Validación experimental** mediante osciloscopio digital custom

### Limitaciones Identificadas

1. **Frecuencia de salida limitada:** 3.006 Hz debido al delay implementado
2. **Resolución limitada:** 8 bits vs. DAC comerciales de 12-16 bits
3. **Dependencia del filtrado externo** para aplicaciones prácticas

### Recomendaciones Futuras

1. **Reducir el delay a 390 µs** para alcanzar frecuencia objetivo de 10 Hz
2. **Implementación de PWM de mayor resolución** (10-12 bits)
3. **Desarrollo de filtros analógicos integrados**
4. **Expansión a múltiples canales de salida**

---

## Instalación y Uso

### Requisitos

- Arduino IDE 1.8.0 o superior
- Arduino Uno o compatible
- Componentes del circuito (ver lista de materiales)

### Pasos de Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/ebla08/Examen-Final-DIGI-II.git
   ```

2. **Abrir el proyecto** en Arduino IDE

3. **Cargar el código** al Arduino Uno

4. **Conectar el circuito** según el esquema proporcionado

5. **Usar el pulsador** en Pin 2 para cambiar entre formas de onda

---

## Estructura del Proyecto

```
Examen-Final-DIGI-II/
├── README.md
├── DAC_PWM.ino
├── docs/
│   ├── informe_tecnico.pdf
│   └── esquematico.png
└── examples/
    └── test_signals.ino
```

---

## Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork del proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit de tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

---

## Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

---

## Autor

**Edward Barrios Quiroga**
- Carrera: Ingeniería en Telecomunicaciones
- Curso: Electrónica Digital II

---

## Referencias

- [Arduino Reference](https://www.arduino.cc/reference/en/)
- [ATmega328P Datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf)
- [PWM Theory and Applications](https://en.wikipedia.org/wiki/Pulse-width_modulation)

---

<div align="center">

**Si este proyecto te fue útil, considera darle una estrella ⭐**

</div>
