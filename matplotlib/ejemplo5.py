import matplotlib.pyplot as plt

# Etiquetas de las categorías
categorias = ["A", "B", "C", "D", "E"]

# Valores correspondientes a cada categoría
valores = [30, 15, 20, 10, 25]

# Crear el gráfico de torta
plt.pie(valores, labels=categorias)

# Agregar título
plt.title("Gráfico de Torta")

# Mostrar el gráfico
plt.show()
