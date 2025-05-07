#Chay Edelmy
import numpy as np
from scipy.interpolate import lagrange
import time

# Definición de los puntos de interpolación
x_points = np.array([1.0, 2.5, 4.0, 5.5])  # Profundidades en cm
y_points = np.array([85, 78, 69, 60])        # Temperaturas en °C

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
        # Mostrar el término calculado para cada i
        print(f"Término para i={i}: {term:.6f}")
    return result

# Profundidad a evaluar
x_interpolate = 3.0

# Medir tiempo de inicio
tiempo_inicio = time.time()

# Calcular el valor interpolado
temperatura_interpolada = lagrange_interpolation(x_interpolate, x_points, y_points)

# Crear una función "exacta" usando scipy para comparación
poly_exacto = lagrange(x_points, y_points)
temperatura_exacta = poly_exacto(x_interpolate)

# Calcular error
error = abs(temperatura_exacta - temperatura_interpolada)

# Medir tiempo de procesamiento
tiempo_final = time.time()
tiempo_total = (tiempo_final - tiempo_inicio) * 1000  # Convertir a milisegundos

# Imprimir resultados intermedios
print("RESULTADOS INTERMEDIOS:")
print("-" * 50)
print(f"Profundidad a evaluar: {x_interpolate:.2f} cm")
print(f"Temperatura interpolada: {temperatura_interpolada:.6f} °C")
print(f"Temperatura exacta: {temperatura_exacta:.6f} °C")
print(f"Error absoluto: {error:.6f} °C")
print(f"Tiempo total de procesamiento: {tiempo_total:.2f} milisegundos")
print("-" * 50)
