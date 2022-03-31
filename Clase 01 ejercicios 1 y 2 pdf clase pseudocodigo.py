Ejercicio 1 
Leer un número N y luego leer N número. Indicar cuál fue el mayor.

Algotirmo Mayor

Escribitr "Maquina detercota de numeros mayores"
Escribir "Ingrese un numero:

Lerr numero
numMayor <- 0

Para i <- 0 hasta N hacer
leer valor

    si valor > numMayor entonces
        numMayor <- valor
    fin si

Fin PARA

Escribir "El resultado mas grande es", numMayor
Fin Algoritmo 

-----------
Ejercicio 2
Leer un número e indicar si es primo.

Escribir "Detector de numeros primos"
Escribir "Ingrese un numero para verificar si es primo"
leer numero

esprimo <- false

PARA i <- 2 hasta (numero-1) hacer
    resto = 0 entonces
        esprimo <- verdadero       
Fin si

Fin PARA

si resto = 0
    Escribir "Felicidades , su numero es primo"
si no
    Escribir "Lo siento, su numero no es primo"
Fin si

fin Algoritmo    
