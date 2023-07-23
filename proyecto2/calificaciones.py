# 1.	Escribir un programa que almacene las materias de un curso (por ejemplo IA, BDD, Matemáticas, inglés, POO) en una lista, pregunte al usuario la calificación obtenida en cada materia y después:
# a.	Muestre en pantalla con el mensaje
# i.	En <materia> has obtenido <calificación>
# En donde cada <materia> es cada una de las materias de la lista y <calificación> cada una de las calificaciones introducidas por el usuario.


def obtener_calificacion(materia):
    while True:
        try:
            calificacion = float(
                input(f"Ingrese la calificación obtenida en {materia}: ")
            )
            return calificacion
        except ValueError:
            print("Error: Ingrese un valor numérico para la calificación.")


def main():
    materias = ["IA", "BDD", "Matematicas", "Ingles", "POO"]
    while True:
        try:
            num_alumnos = int(input("Ingrese el número total de alumnos: "))
            if num_alumnos <= 0:
                raise ValueError
            break
        except ValueError:
            print("Error: Ingrese un número entero mayor que cero.")

    calificaciones = []

    for i in range(num_alumnos):
        print(f"\nAlumno {i+1}:")
        calif_alumno = []
        for materia in materias:
            calificacion = obtener_calificacion(materia)
            calif_alumno.append(calificacion)
            print(f"En {materia} has obtenido {calificacion}.")

        calificaciones.append(calif_alumno)

    print("\nPromedio de cada alumno:")
    for i, calif_alumno in enumerate(calificaciones):
        suma_calificaciones = sum(calif_alumno)
        promedio = suma_calificaciones / len(materias)
        print(f"Alumno {i+1}: Promedio = {promedio:.2f}")


if __name__ == "__main__":
    main()
