precios_frutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranja": 0.70}

print("Frutas disponibles:")
for fruta in precios_frutas:
    print(fruta)

while True:
    fruta = input("Ingrese el nombre de la fruta (o 'salir' para terminar): ")

    if fruta.lower() == "salir":
        break

    try:
        kilos = float(input("Ingrese el número de kilos: "))
        if fruta in precios_frutas:
            precio_total = precios_frutas[fruta] * kilos
            print(f"El precio de {kilos} kilos de {fruta} es: {precio_total}")
        else:
            print("La fruta no está en la lista de precios.")
    except ValueError:
        print("Error: Ingrese un número válido para los kilos.")

print("Programa terminado.")
