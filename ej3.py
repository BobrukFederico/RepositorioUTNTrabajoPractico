#3 - Especializar la función del punto 1 para que valide el número en un rango determinado
#pasado por parámetro “desde”-“hasta”

def mostrar_pantalla_modificada(numero, min, max):
    if numero >= min and numero <= max:
        print("Esta dentro del rango")
    else:
        print("No esta dentro del rango")