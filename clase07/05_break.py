#sumar todos los elementos de la lista, hasta que encontramos un elemento -1
lista = [3,1,5,6,-1,3,5,7]

suma = 0
for numero in lista:
    if numero == -1:
        break
    suma = suma + numero
    print("resultado parcial: ",suma)
print("resultado final: ",suma)