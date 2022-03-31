#Ejercicio 04
'''Solicitar el ingreso de un mes y un año e informar la cantidad de días del mes, considerando los años bisiestos.
Tenga en cuenta que un año bisiesto es aquel dividible por 4, salvo que sea divisible por 100, en cuyo caso también debe ser divisible por 400.'''


mes = int(input("mes"))
anio = int(input("anio"))
esbisiesto = False

if anio%4 == 0 and (anio%400 != 0 or anio%100 ==0):
    esbisiesto = True
    
if mes == 1 or mes ==3 or mes == 5 or mes ==7 or mes ==8 or mes ==10 or mes ==12:
    print(mes, "La cantidad de dias del mes es 31")

elif mes == 4 or mes == 6 or mes ==9 or mes ==11:
    print(mes, "La cantidad de dias del mes es 30")


elif esbisiesto == True and mes ==2:  #febrero  bisiesto
    print(mes, "La cantidad de dias del mes es 29")
elif mes == 2:
    print(mes, "La cantidad de dias del mes es 28")   #febrero NO bisiesto
else:
    print("Dato ingresado invalido")

