import matplotlib.pyplot as plt

# Datos para el Eje X (Tiempo)
x = [1, 2, 3, 4, 5]

# Datos para el eje y (Valores)
y = [2, 4, 6, 8, 10]

# Crear el grafico de linea
plt.plot(x, y)

# Agregar etiquetas y titulo
plt.xlabel("Tiempo")  # Etiqueta del eje x
plt.ylabel("Valores")  # Etiqueta del eje y
plt.title("Grafico de Lineas")

# Mostrar el Grafico
plt.show()
