#Chay Edelmy
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
import time

# Definición de los puntos de interpolación
x_points = np.array([2.0, 4.0, 6.0, 8.0])  # Altitudes en km
y_points = np.array([2500, 2300, 2150, 2050])  # Consumo en kg/h

# Función de interpolación de Lagrange
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Altitud a evaluar
x_interpolate = 5.0

# Medir tiempo de inicio
tiempo_inicio = time.time()

# Calcular el valor interpolado
consumo_interpolado = lagrange_interpolation(x_interpolate, x_points, y_points)

# Crear una función "exacta" usando scipy para comparación
poly_exacto = lagrange(x_points, y_points)
consumo_exacto = poly_exacto(x_interpolate)

# Calcular error
error = abs(consumo_exacto - consumo_interpolado)

# Medir tiempo de procesamiento
tiempo_final = time.time()
tiempo_total = (tiempo_final - tiempo_inicio) * 1000  # Convertir a milisegundos

# Imprimir resultados intermedios
print("RESULTADOS INTERMEDIOS:")
print("-" * 50)
print(f"Altitud a evaluar: {x_interpolate:.2f} km")
print(f"Consumo interpolado: {consumo_interpolado:.6f} kg/h")
print(f"Consumo exacto: {consumo_exacto:.6f} kg/h")
print(f"Error absoluto: {error:.6f} kg/h")
print(f"Tiempo total de procesamiento: {tiempo_total:.2f} milisegundos")
print("-" * 50)

# Graficar los datos y la interpolación
x_values = np.linspace(2.0, 8.0, 100)
y_values = [lagrange_interpolation(x, x_points, y_points) for x in x_values]

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="Interpolación de Lagrange", color="blue")
plt.scatter(x_points, y_points, color="red", label="Datos originales", s=100)
plt.scatter(x_interpolate, consumo_interpolado, color="green", 
            label=f"Consumo estimado (x={x_interpolate} km)", s=100)
plt.xlabel("Altitud (km)")
plt.ylabel("Consumo (kg/h)")
plt.title("Interpolación del Consumo de Combustible en Función de la Altitud")
plt.legend()
plt.grid(True)
plt.show()
