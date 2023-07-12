import matplotlib.pyplot as plt
import numpy as np

# Datos para el gráfico de caja
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

# Crear el gráfico de caja
plt.boxplot(data)

# Agregar etiquetas y título
plt.xlabel("Variables")
plt.ylabel("Valores")
plt.title("Gráfico de Caja")

# Mostrar el gráfico
plt.show()
