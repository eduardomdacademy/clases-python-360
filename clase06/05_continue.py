#Programa que imprime todos los numeros del 1 al 100 que sean pares
numero = 0
while numero < 100:
    numero = numero +1
    if numero%2 != 0:
        continue
    print(numero)