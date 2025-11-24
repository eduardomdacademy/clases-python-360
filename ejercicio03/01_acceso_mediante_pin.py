pin_correcto = "1234"

intentos = 0
pin_aceptado = False
while intentos < 3:
    intentos += 1
    pin_ingresado = input("Ingresa el pin:" )
    if pin_ingresado == pin_correcto:
        print("PIN ACEPTADO")
        pin_aceptado = True
        break
    else:
        print("PIN INCORRECTO")
if pin_aceptado == False:
    print("Has superado la cantidad de intentos!")
