def crear_diccionario():
    diccionario = {}
    palabras = input(
        "Introduce las palabras en español e inglés separadas por dos puntos, y cada par separado por comas: "
    )
    pares = palabras.split(",")

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
print("Palabras añadidas al diccionario:", list(diccionario.keys()))
frase_traducida = traducir_frase(diccionario)
print("Traducción:", frase_traducida)
