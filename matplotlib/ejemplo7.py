import matplotlib.pyplot as plt
import numpy as np

# Datos para el gráfico de bigotes
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Crear el gráfico de bigotes
plt.boxplot(data, vert=False)

# Agregar etiquetas y título
plt.xlabel("Valores")
plt.ylabel("Variables")
plt.title("Gráfico de Bigotes")

# Mostrar el gráfico
plt.show()
