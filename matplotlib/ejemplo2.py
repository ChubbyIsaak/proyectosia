import matplotlib.pyplot as plt

# Datos para el eje x
x = [1, 2, 3, 4, 5]

# Datos para el eje y
y = [2, 4, 6, 8, 10]

# Crear el gráfico de dispersión
plt.scatter(x, y)

# Agregar etiquetas y título
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráfico de Dispersión")

# Mostrar el gráfico
plt.show()
