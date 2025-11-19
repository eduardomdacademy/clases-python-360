#Solicitar que el usuario ingrese un numero entre 1-100
#determinar si el numero ingresado es primo
#un numero es primo si no es divisible por ningun otro numero excepto 1
#podemos determinar que un numero es divisible si el modulo(%) es igual a 0

while True:
    valor_string = input("Ingresa un numero del 1 al 100: ")
    if valor_string.isnumeric():
        n = int(valor_string)
        if n >= 1 and n <= 100:
            break
es_primo = True
for i in range(2,n):
    if n%i==0:
        print("El numero es divisible por ", i)
        print("el numero no es primo")
        es_primo = False
        break
    print("El numero NO es divisible por ", i)

if es_primo == True:
    print("El numero es primo")