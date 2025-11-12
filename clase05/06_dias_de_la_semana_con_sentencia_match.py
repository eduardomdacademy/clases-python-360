dia_string = input("ingresa el valor entre 1 a 7: ")
if dia_string.isnumeric():
    dia_numerico = int(dia_string)
    match dia_numerico:
        case 1:
            print("Lunes")
        case 2:
            print("Martes")
        case 3:
            print("Miercoles")
        case 4:
            print("Jueves")
        case 5:
            print("Viernes")
        case 6:
            print("Sabado")
        case 7:
            print("Domingo")
        
else:
    print("ERROR! el valor deber ser numerico")