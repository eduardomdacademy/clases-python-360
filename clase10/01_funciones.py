def suma(valor1, valor2):
    print("llamamos a la funcion suma con parametros:", valor1, valor2)
    resultado = valor1 + valor2
    return resultado

resultado1 = suma(4,3)
print(resultado1)

resultado2 = suma(resultado1, 2)
print(resultado2)