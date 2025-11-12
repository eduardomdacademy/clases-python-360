a = 23
#queremos saber si a es par y mayor que 10
if a%2 == 0: #a modulo 2 solamente sera 0 si a es divisible entre 2, lo cual es la definicion de un numero par
    print("el numero es par")
    if a > 10:
        print("el numero tambien es mayor a 10")
    else:
        print("el numero no es mayor a 10")
    print("esta linea ya esta afuera del if anidado")
else:
    print("el numero no es par")
print("esta linea ya esta afuera del if")