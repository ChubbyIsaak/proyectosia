def main():
    numeros_ganadores = []
    cantidad_numeros = int(input("Ingrese la cantidad de números ganadores: "))

    for i in range(cantidad_numeros):
        numero = int(input(f"Ingrese el número ganador {i + 1}: "))
        numeros_ganadores.append(numero)

    numeros_ganadores.sort(reverse=True)

    print("Números ganadores (de mayor a menor):")
    for numero in numeros_ganadores:
        print(numero)


if __name__ == "__main__":
    main()
