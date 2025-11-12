
año = 2025
mes = 2
dia = 29

if mes == 1:
    if dia > 0 and dia <= 31:
        print("La fecha es válida")
    else:
        print("la fecha es inválida")
elif mes == 2:
    if año%4 == 0 and año%400 != 0: #El año es bisiesto
        if dia > 0 and dia <= 29:
            print("La fecha es válida")
        else:
            print("la fecha es inválida")
    else: #el año no es bisiesto
        if dia > 0 and dia <= 28:
            print("La fecha es válida")
        else:
            print("la fecha es inválida")
elif mes == 3:
    if dia > 0 and dia <= 31:
        print("La fecha es válida")
    else:
        print("la fecha es inválida")
elif mes == 4:
    if dia > 0 and dia <= 30:
        print("la fecha es válida")
    else:
        print("la fecha es inválida")
elif mes == 5:
    if dia > 0 and dia <= 31:
        print("la fecha es válida")
    else:
        print("la fecha es inválida")
elif mes == 6:
    if dia > 0 and dia <= 30:
        print("la fecha es válida")
    else:
        print("la fecha es inválida")
elif mes == 7:
    if dia > 0 and dia <= 31:
        print("la fecha es válida")
    else:
        print("la fecha es inválida")
elif mes == 8:
    if dia > 0 and dia <= 31:
        print("la fecha es válida")
    else:
        print("la fecha es inválida")
elif mes == 9:
    if dia > 0 and dia <= 30:
        print("la fecha es válida")
    else:
        print("la fecha es inválida")
elif mes == 10:
    if dia > 0 and dia <= 31:
        print("la fecha es válida")
    else:
        print("la fecha es inválida")
elif mes == 11:
    if dia > 0 and dia <= 30:
        print("la fecha es válida")
    else:
        print("la fecha es inválida")
elif mes == 12:
    if dia > 0 and dia <= 31:
        print("la fecha es válida")
    else:
        print("la fecha es inválida")
else:
    print("el mes es invalido")