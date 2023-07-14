import matplotlib.pyplot as plt

# Etiquetas de las categorías
categorias = [
    "Geografia  Aprobados",
    "Geografia Reprobados",
    "Matematicas Aprobados",
    "Matematicas Reprobados",
    "Lenguas Aprobados",
    "Lenguas Reprobados",
]

# Valores correspondientes a cada categoría
valores = [25, 5, 15, 17, 29, 1]

# Crear el gráfico de torta
plt.pie(valores, labels=categorias)

# Agregar título
plt.title("Alumnos Aprobados/Reprobados")

# Mostrar el gráfico
plt.show()
