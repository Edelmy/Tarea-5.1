import numpy as np
from scipy.interpolate import lagrange
import time

# Definición de los puntos de interpolación
x_points = np.array([0.5, 1.0, 1.5, 2.0])
y_points = np.array([1.2, 2.3, 3.7, 5.2])

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

# Puntos a evaluar
x_interpolar = [1.25, 0.75, 1.75]  # Puedes agregar más puntos aquí

# Medir tiempo de inicio
tiempo_inicio = time.time()

# Imprimir encabezado de resultados
print("RESULTADOS:")
print("-" * 50)

# Evaluar cada punto
for x in x_interpolar:
    # Valor interpolado
    deformacion_interpolada = lagrange_interpolation(x, x_points, y_points)

    # Crear una función "exacta" usando scipy para comparación
    poly_exacto = lagrange(x_points, y_points)
    deformacion_exacta = poly_exacto(x)

    # Calcular error
    error = abs(deformacion_exacta - deformacion_interpolada)

    # Imprimir resultados para cada punto
    print(f"Para x = {x:.2f} m:")
    print(f"  Valor interpolado: {deformacion_interpolada:.6f} mm")
    print(f"  Valor exacto: {deformacion_exacta:.6f} mm")
    print(f"  Error absoluto: {error:.6f} mm")
    print("-" * 50)

# Medir tiempo de procesamiento
tiempo_final = time.time()
tiempo_total = (tiempo_final - tiempo_inicio) * 1000  # Convertir a milisegundos

# Imprimir tiempo total de procesamiento
print(f"Tiempo total de procesamiento: {tiempo_total:.2f} milisegundos")
