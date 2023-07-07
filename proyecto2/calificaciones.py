def main():
    materias = ["IA", "BDD", "Matematicas", "Ingles", "POO"]
    calificaciones = []

    for materia in materias:
        calificacion = input(f"Ingrese la calificación obtenida en {materia}: ")
        calificaciones.append(calificacion)

    print("Calificaciones obtenidas:")
    for i in range(len(materias)):
        print(f"En {materias[i]} has obtenido {calificaciones[i]}")


if __name__ == "__main__":
    main()
