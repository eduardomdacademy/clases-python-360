numeros = [2,3,4,-41,5,10,0]

def procesar_numero(numero):
    if numero == 0:
        raise ZeroDivisionError("El numero no puede ser 0")
    if numero <0 :
        raise Exception("El numero no puede ser negativo")
    print(numero)
    
for numero in numeros:
    try:
        procesar_numero(numero)
    except ZeroDivisionError:
            raise Exception("el numero no puede ser 0")
    except:
        procesar_numero(numero*(-1))
    