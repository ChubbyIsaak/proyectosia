import matplotlib.pyplot as plt

categorias = [
    "Geografia Aprobados"
    "Geografia Reprobados"
    "Matematicas Aprobados"
    "Matematicas Reprobados"
    "Lenguas Aprobados"
    "Lenguas Reprobados"
]

valores = [25, 5, 15, 17, 29, 1]

plt.pie(valores, labels=categorias)

plt.title("Alumnos Aprobados y Reprobados de la Maestra Ana")

plt.show()