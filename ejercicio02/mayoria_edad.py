# Ejercicio 1:
# Escribe un programa que solicite al usuario que ingrese su nombre y luego su edad, almacene ambas como variables.
# Luego debe determinar si el usuario es o no menor de edad e imprimir un mensaje acorde.
# 	Ej: “Eduardo es mayor de edad”
# Tip: Recuerda que al recibir la edad del input del usuario debemos intentar convertirla a números usando int()

nombre = input("Ingrese el nombre: ")
edad_string = input("Ingrese la edad:")
if not edad_string.isnumeric():
    print("ERROR! la edad debe ser un numero")
else:
    edad_numero = int(edad_string)
    if edad_numero < 18:
        mensaje = nombre + " es menor de edad"
        print(mensaje)
    else:
        mensaje = nombre + " es mayor de edad"
        print(mensaje)
