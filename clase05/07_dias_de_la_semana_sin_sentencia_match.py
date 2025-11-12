dia_string = input("ingresa un numero del 1 al 7: ")
if dia_string.isnumeric():
    dia_numero = int(dia_string)
    if dia_numero == 1:
        print("Lunes")
    elif dia_numero == 2:
        print("Martes")
    elif dia_numero == 3:
        print("Miercoles")
    elif dia_numero == 4:
        print("Jueves")
    elif dia_numero == 5:
        print("Viernes")
    elif dia_numero == 6:
        print("Sabado")
    elif dia_numero == 7:
        print("Domingo")
    else:
        print("ERROR! El numero debe ser del 1 al 7")
else:
    print("ERROR! el valor ingresado debe ser numerico")