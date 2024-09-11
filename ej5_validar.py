def descuento(num1):
    desc = num1 * 0.05
    return num1 - desc

def validar(numero1):
    if 10 < numero1 < 100:
        return True
    else:
        return False
