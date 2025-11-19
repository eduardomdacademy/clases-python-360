# El programa debe solicitar al usuario un numero N del 1 al 100
# el programa debe imprimir los primeros N numeros de fibonacci
# La serie de numeros de fibonaccio empieza con 0, luego 1, y todos los siguiente son igual a la suma de los dos anteriores
while True:
    valor_string = input("Ingresa un numero del 1 al 100: ")
    if valor_string.isnumeric():
        n = int(valor_string)
        if n >= 1 and n <= 100:
            break

PRIMER_NUMERO_FIBONACCI = 0
SEGUNDO_NUMERO_FIBONACCI = 1

penultimo = PRIMER_NUMERO_FIBONACCI
ultimo =  SEGUNDO_NUMERO_FIBONACCI
print("Fibonacci numero 1: " ,PRIMER_NUMERO_FIBONACCI)
if n >= 2:
    print("Fibonacci numero 2: " ,SEGUNDO_NUMERO_FIBONACCI)
for numero in range(3,n+1):
    nuevo_numero = ultimo + penultimo
    print("Fibonacci numero " + str(numero), ": " ,nuevo_numero)
    penultimo = ultimo
    ultimo = nuevo_numero
    