#funcion que escriba los primeros N numeros de fibonacci
def imprimir_fibonacci(contador,cantidad_maxima, penultimo, ultimo):
    nuevo_numero = penultimo + ultimo
    print(nuevo_numero)
    contador = contador + 1
    if contador > cantidad_maxima:
        return
    else:
        imprimir_fibonacci(contador, cantidad_maxima, ultimo, nuevo_numero)
    

PRIMER_NUMERO_FIBONACCI = 0
SEGUNDO_NUMERO_FIBONACCI = 1
print(PRIMER_NUMERO_FIBONACCI)
print(SEGUNDO_NUMERO_FIBONACCI)
cantidad_de_numeros_a_imprimir = 10
imprimir_fibonacci(0,cantidad_de_numeros_a_imprimir,PRIMER_NUMERO_FIBONACCI,SEGUNDO_NUMERO_FIBONACCI)