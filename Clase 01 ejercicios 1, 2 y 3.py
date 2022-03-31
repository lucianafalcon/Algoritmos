#Ejercicio 01
'''Escribir un programa que solicite el ingreso de dos números y luego informe cuál es el mayor de los número ingresados.
Suponer que siempre los números ingresados serán distintos.'''

'''Ahora, tomá el ejercicio anterior y considerá que el usuario podría ingresar dos veces el mismo número.'''

numero1 = int(input("numero "))
numero2 = int(input("numero "))
if numero1 > numero2:
    print(numero1, " 1 es mayor")
elif numero2 > numero1:
    print(numero2, " es mayor")
else:
    print(numero1, "Es igual a", numero2)

-------------
#Ejercicio 02
'''Escribir un programa que solicite el ingreso de un número que representa un mes, e informe el nombre del mes.
Por ejemplo, si el usuario ingresa "1", se deberá mostrar: "Mes ingresado: Enero"
En caso que el número de mes ingresado por el usuario no sea válido, deberá mostrar "Mes Ingresado: Inválido".'''  


numero1 = int(input("Ingrese un numero del 1 al 6:"))

if numero1 == 1:
    print("Es enero")
elif numero1 ==2:
    print("Es febrero")
elif numero1 ==3:
    print("Es marzo")
elif numero1 ==4:
    print("Es abril")
elif numero1 ==5:
    print("Es mayo")
elif numero1 ==6:
    print("Es junio")
else:
    print("Mes invalido")
    




