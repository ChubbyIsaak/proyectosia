import matplotlib.pyplot as plt

# Categorías
categorias = ["A", "B", "C", "D", "E"]

# Valores
valores = [15, 8, 12, 10, 7]

# Crear el gráfico de barras
plt.bar(categorias, valores)

# Agregar etiquetas y título
plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.title("Gráfico de Barras")

# Mostrar el gráfico
plt.show()
