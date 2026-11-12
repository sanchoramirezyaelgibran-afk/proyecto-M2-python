"""Proyecto 2: Validación y operaciones.

Une los retos de Cuadrantes y Longitud de palabra en un solo
programa con menú.
"""

# TUPLA: nombres fijos de los cuadrantes, se accede con índices
CUADRANTES = ("Cuadrante I", "Cuadrante II", "Cuadrante III", "Cuadrante IV")

# LISTA: guarda las palabras intentadas durante toda la sesión
intentos = []


def pedir_coordenada(nombre):
    """Pide una coordenada y repite hasta que sea entero distinto de 0."""
    while True:
        try:
            valor = int(input(f"Ingresa la coordenada {nombre}: "))
        except ValueError:
            print("Error: escribe un número entero.")
            continue
        if valor == 0:
            print(f"Error: {nombre} no puede ser 0. Intenta de nuevo.")
        else:
            return valor


def reto_cuadrantes():
    """Reto 1: dice en qué cuadrante cae el punto (X, Y)."""
    x = pedir_coordenada("X")
    y = pedir_coordenada("Y")

    # Elegimos el índice de la tupla según los signos
    if x > 0 and y > 0:
        indice = 0
    elif x < 0 and y > 0:
        indice = 1
    elif x < 0 and y < 0:
        indice = 2
    else:
        indice = 3

    print(CUADRANTES[indice])


def reto_longitud():
    """Reto 2: cuenta las letras de una palabra válida."""
    palabra = input("Ingresa una palabra: ")
    intentos.append(palabra)

    # Se repite mientras la palabra tenga números o espacios
    while not palabra.isalpha():
        print("Error: solo se permiten letras, sin espacios ni números.")
        palabra = input("Ingresa una palabra nueva: ")
        intentos.append(palabra)

    print(f"La palabra tiene {len(palabra)} letras")


def main():
    """Menú principal: repite hasta que el usuario elija salir."""
    while True:
        print("\n=== MENÚ ===")
        print("1. Cuadrantes")
        print("2. Longitud de palabra")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            reto_cuadrantes()
        elif opcion == "2":
            reto_longitud()
        elif opcion == "3":
            print("Palabras intentadas:", intentos)
            break
        else:
            print("Opción inválida. Elige 1, 2 o 3.")


if __name__ == "__main__":
    main()