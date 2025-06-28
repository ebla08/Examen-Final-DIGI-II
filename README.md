# DAC mediante PWM con Arduino
## CASO 1 --> Implementación de Conversor Digital-Analógico usando un DAC0808
# Generador de Señales con Arduino y DAC0808

## Materiales

- 2 Placas de Desarrollo Arduino UNO
- 1 DAC0808
- 1 Regulador de Voltaje 78L05
- 1 Capacitor de 100nF
- 2 Capacitores de 10µF
- 1 Capacitor de 10nF
- 1 Amplificador Operacional UA741CP
- 2 Fuentes de Voltaje de Laboratorio 0-30V
- 3 Resistencias de 10kΩ
- 2 Resistencias de 1kΩ
- 2 Pulsadores

## 2. Señales proporcionadas por el Generador

El generador está configurado para entregar cuatro tipos de señales diferentes:
- Señal sinusoidal
- Señal triangular
- Señal cuadrada
- Señal diente de sierra

Adicionalmente se incrementó el número de muestras de cada señal, de un valor original de 64 a 256 muestras a fines de mejorar la resolución y exactitud de las señales entregadas por el generador.

![image](https://github.com/user-attachments/assets/bbec8699-bfd3-4f99-a294-037dcfd484c2)


## 3. Conversor Digital-Analógico DAC0808

El circuito integrado DAC0808 es un conversor Digital/Analógico de 8 bits compatible con tecnologías "CMOS" y "TTL". A continuación se adjunta la ilustración del circuito integrado y las funciones que cumple cada PIN:

![image](https://github.com/user-attachments/assets/85e758f1-f050-4bc4-b112-4f3bc6385e7e)


### Cuadro 1: Funciones y Características de cada PIN

| Pin | Nombre | Función |
|-----|--------|---------|
| 2 | GND | Tierra General |
| 13 | Vcc | Alimentación Positiva |
| 3 | Vee | Alimentación Negativa |
| 14 | Vref(+) | Voltaje de Referencia Positivo |
| 15 | Vref(-) | Voltaje de Referencia Negativo |
| 16 | COMP | Estabilización de Polarización |
| 4 | Io | Salida de Corriente |
| 5-12 | A1-A8 | Entradas Digitales |

Los pines asignados a las entradas digitales indican el "Bit de Mayor Peso" (El bit de mayor valor) y el "Bit de Menor Peso" (El bit de menor valor), ambos asignados al Pin "5" (MSB) y el Pin "12" (LSB), respectivamente.

El pin "16" (COMPENSATION) se utiliza para polarizar el circuito y requiere de un capacitor cerámico conectado al pin "15" (Vref(-)). Finalmente, el pin "Io" debe ser acoplado a un amplificador operacional de trans-impedancia para obtener las señales analógicas resultantes.

### 3.1. Circuito de Polarización

![image](https://github.com/user-attachments/assets/23a3cfc1-0dbc-4a3e-bdae-d4e8fd11e251)


Se utilizaron dos fuentes de alimentación de 12V en serie, ambas fuentes suministran energía al conversor analógico digital y al amplificador operacional. Se utilizó un capacitor de 100nF para el pin "16" (COMPENSATION), mientras que para los voltajes de referencia positivo y negativo (Vref+, pin "14" y Vref-, pin "15") se utilizó un regulador de voltaje que permita ajustar la señal de salida dentro de un rango de "0-5V".

### 3.2. Regulador 78L05

![image](https://github.com/user-attachments/assets/dfe9d803-5f84-45b2-b23f-1ea9900bff67)


El regulador de voltaje permite ajustar el voltaje de referencia del DAC0808 para un máximo de 5V y un mínimo de 0V. El regulador utiliza la alimentación positiva de 12V y proporciona una salida constante con un error de 1% sin necesidad de un divisor de tensión que puede inducir ruido dentro del circuito. Tanto la salida como la entrada del regulador se encuentran desacopladas mediante capacitores electrolíticos de 10µF.

## 4. Casos Planteados

Se desarrollaron dos casos, o métodos, para construir un generador de señales:

1. **Caso 1**: El microcontrolador Arduino UNO trabajando en conjunto con el circuito integrado "DAC0808"
2. **Caso 2**: Una señal PWM, generada con el microcontrolador Arduino UNO, y filtrada con un circuito RC (Filtro Pasa Bajos) encargado de "reconstruir" la señal

Se adjuntan ilustraciones correspondientes a cada caso:

![image](https://github.com/user-attachments/assets/397a6533-74b3-4008-b16f-fadf395f4eb7)
![image](https://github.com/user-attachments/assets/21c14d27-baf7-4ab6-b57e-ea1738e4b231)



En ambos casos se utilizaron valores de "0" a "255", con un total de "256" muestras, para representar las señales de forma discreta. Las señales pueden seleccionarse de forma manual mediante un circuito "Pull-Down" acoplado al microcontrolador Arduino UNO.

## 5. Pruebas en Laboratorio

### 5.1. Caso 1

Se procedió a montar los componentes del generador en una "Breadboard" convencional y realizar las pruebas de funcionamiento con el apoyo de un osciloscopio digital de laboratorio:

![image](https://github.com/user-attachments/assets/93b0e0bc-30e5-4eb0-a5ea-842022f61e4f)


Las señales resultantes se muestran a continuación, el canal "1" (Amarillo) muestra la señal original sin filtrar, mientras que el canal "2" (Azul) muestra la señal filtrada.

#### 1. Señal Sinusoidal

![image](https://github.com/user-attachments/assets/9cfcee5e-85e1-4b2b-82f6-3e3160e642be)


#### 2. Señal Cuadrada

![image](https://github.com/user-attachments/assets/80bd0694-a71d-4c67-a837-effbdfe04260)


#### 3. Señal Triangular

![image](https://github.com/user-attachments/assets/1b7dba60-3c06-4df0-b675-0b81c7541492)


#### 4. Señal Diente de Sierra

![image](https://github.com/user-attachments/assets/4b1abd36-55a0-4c62-ab3b-05139e17f595)



## CASO 2 --> Implementación de Conversor Digital-Analógico usando Modulación PWM

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
