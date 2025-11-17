# Ejercicio Bonus:
# Escribir un programa de calculadora
# Solicitar al usuario 2 números y guardarlos en variables
# Solicitar al usuario que escoja una operación: 
# •	Suma
# •	Resta
# •	multiplicación
# •	división
# Realice la operación escogida usando los dos numero recibidos e imprima el resultado


valor_1_string = input("Ingresa el numero 1: ")
if valor_1_string.isnumeric:
    valor_1 = int(valor_1_string) 
    valor_2_string = input("Ingresa el numero 2: ")
    if valor_2_string.isnumeric:
        valor_2  = int(valor_2_string)
        print("OPERACION:")
        print("1 - SUMA")
        print("2 - RESTA")
        print("3 - MULTIPLICACION")
        print("4 - DIVISION")
        opcion_string = input("INGRESA LA OPCION QUE DESEAS UTILIZAR (1-4): ")
        if opcion_string.isnumeric:
            opcion = int(opcion_string)
            match opcion:
                case 1:
                    resultado = valor_1 + valor_2
                    mensaje = str(valor_1) + " + " + str(valor_2) + " = " + str(resultado)
                    print(mensaje)
                case 2:
                    resultado = valor_1 - valor_2
                    mensaje = str(valor_1) + " - " + str(valor_2) + " = " + str(resultado)
                    print(mensaje)
                case 3:
                    resultado = valor_1 * valor_2
                    mensaje = str(valor_1) + " * " + str(valor_2) + " = " + str(resultado)
                    print(mensaje)
                case 4:
                    if valor_2 != 0:
                        resultado = valor_1 / valor_2
                        mensaje = str(valor_1) + " / " + str(valor_2) + " = " + str(resultado)
                        print(mensaje)
                    else:
                        print("ERROR! no se puede realizar la division entre 0")
                case _:
                    print("ERROR! la opcion debe estar entre 1 a 4")

        else:
            print("ERROR! la opcion debe ser un numero")
    else:
        print("ERROR! el valor debe ser un numero")
else:
    print("ERRRO! el valor debe ser un numero")