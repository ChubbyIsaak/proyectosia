import matplotlib.pyplot as plt

# Datos para el histograma
data = [1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5]

# Crear el histograma
plt.hist(data)

# Agregar etiquetas y título
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.title("Histograma")

# Mostrar el gráfico
plt.show()
