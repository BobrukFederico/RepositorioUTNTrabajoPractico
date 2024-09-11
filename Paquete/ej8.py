def calcular_horas_trabajadas(horas_trabajadas, año_de_antiguedad):
    salario_total = horas_trabajadas * 10 * (1+(año_de_antiguedad * 0.03))
    return salario_total


def calcular_productividad(artefactos_producidos, horas_trabajo):
    productividad = artefactos_producidos / horas_trabajo
    return productividad

def reporte(nombre,edad,salario_total, productividad):
    print(f"Nombre {nombre}")
    print(f"Edad: {edad}")
    print(f"Salario total: {salario_total}")
    print(f"Productividad: {productividad}")