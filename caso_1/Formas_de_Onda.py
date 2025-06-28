import numpy as np
import matplotlib.pyplot as plt

N = 64  # número de muestras por ciclo

# Generar onda seno
onda_seno = [int(127.5 + 127.5 * np.sin(2 * np.pi * n / N)) for n in range(N)]

# Generar onda triangular
onda_triangular = [int((n * 255 / (N//2)) if n < N//2 else 255 - ((n - N//2) * 255 / (N//2))) for n in range(N)]

# Generar onda cuadrada
onda_cuadrada = [255 if n < N//2 else 0 for n in range(N)]

# Onda Diente de Sierra
onda_diente_sierra = [int((n * 255) / (N//2)) if n < N//2 else ((n - N//2) * 255 // (N//2)) for n in range(N)]

# Mostrar como lista (útil para copiar en Arduino)
print("Onda seno:")
print(onda_seno)
print("\nOnda triangular:")
print(onda_triangular)
print("\nOnda cuadrada:")
print(onda_cuadrada)
print("\nOnda diente de sierra:")
print(onda_diente_sierra)

# Graficar
plt.figure(figsize=(10,6))
plt.plot(onda_seno, label='Senoidal')
plt.plot(onda_triangular, label='Triangular')
plt.plot(onda_cuadrada, label='Cuadrada')
plt.plot(onda_diente_sierra, label='Sierra')
plt.title("Formas de Onda Digitales")
plt.xlabel("Muestra")
plt.ylabel("Valor (0-255)")
plt.legend()
plt.grid()
plt.show()