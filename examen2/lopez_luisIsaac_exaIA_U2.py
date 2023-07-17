def crear_diccionario():
    diccionario = {}
    palabras = input(
        "Introduce las 15 palabras en español e inglés separadas por dos puntos, y cada par separado por comas: "
    )
    pares = palabras.split(",")

    if len(pares) != 15:
        print("Error: Debes ingresar exactamente 15 palabras separadas por comas.")
        return diccionario

    for par in pares:
        try:
            palabra, traduccion = par.split(":")
            diccionario[palabra.strip()] = traduccion.strip()
        except ValueError:
            print(
                f"Error en el par '{par}': Debes ingresar las palabras separadas por dos puntos."
            )

    return diccionario


def traducir_frase(diccionario):
    frase = input("Introduce una frase en español: ")
    palabras = frase.split(" ")
    traduccion = []

    for palabra in palabras:
        if palabra in diccionario:
            traduccion.append(diccionario[palabra])
        else:
            traduccion.append(palabra)

    return " ".join(traduccion)


diccionario = crear_diccionario()
frase_traducida = traducir_frase(diccionario)
print("Traducción:", frase_traducida)
