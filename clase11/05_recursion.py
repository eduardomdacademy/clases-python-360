def funcion_recursiva(valor):
    print(valor)
    nuevo_valor = valor + 1
    funcion_recursiva(nuevo_valor)
    
funcion_recursiva(1)
#esta funcion no tiene forma de terminar, por lo que eventuametnte llegara al limite de 1000 funciones recursivas
#y arrojara un error de RecursionError: maximum recursion depth exceeded exceeded