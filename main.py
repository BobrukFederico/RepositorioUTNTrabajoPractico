import ej1, ej2, ej3, ej5_validar, ej6


#1
num = 5

ej1.mostrar_pantalla(num)

#2

#Par = True, 
#Impar = False
respuesta = ej2.par_impar(5)
print(respuesta)

ej3.mostrar_pantalla_modificada(num,4,15)



#5
num_5 = int(input("Ingrese un numero, entre el 10 al 100: "))

if ej5_validar.validar(num_5):
    desc = ej5_validar.descuento(num_5)
    print(f"El precio final es: {desc}")
else:
    print("Tiene que ser un numero entre el 10 y el 100")


#6
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
while not (10 < numero1 < 100 and 10 < numero2 < 100):
    print("Ambos números deben estar entre 10 y 100.")
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))
operacion = input("Operacion a ingresar [s] [r]")

resultado = ej6.validar2(numero1, numero2, operacion)
print(f"El resultado es: {resultado}")