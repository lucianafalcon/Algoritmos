#Ejercicio 1
'''Mostrar en forma descendente, los números impares entre 0 y 100.'''

for numero in range(99,0,-2):
    print (numero)

------------
#Ejercicio 2
'''Solicitar el ingreso de una serie de números hasta que la suma acumulada supere el valor 1000.
Informar cuantos ingresos se hicieron.'''

numero = in(input("Ingrese nros: "))

acumulador = numero
contador = 1

while suma < 1000:
    numero = int(input"Ingrese otro numero:"))
    acumulador += numero
    contador += 1
    print("Se ingresaron",ingresos, "numeros")
    
-------------
#Ejercicio 03
'''Escribir un programa que solicite el ingreso de un número y luego calcule e informe el factorial del número ingresado.'''

numero = in(input("Ingrese un numero"))

factorial = 1

for num in range(1, numero+1)
    factorial = factorial * num
    print("El factorial del numero ingresado es: ", factrorial)
