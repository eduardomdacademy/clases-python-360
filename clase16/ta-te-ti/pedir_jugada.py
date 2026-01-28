def pedir_jugada(jugador):
    mensaje_fila = "Jugador " + jugador + ", ingresa la fila (0-2): "
    mensaje_columna = "Jugador " + jugador + ", ingresa la columna (0-2): "
    while True:
        try:
            fila = int(input(mensaje_fila))    
            if fila >= 0 and fila <=2:
                break
            else:
                print("La fila debe ser un valor entre 0-2")
        except:
            print("El valor que ingresaste para la fila no es valido")   
    while True:
        try:
            col = int(input(mensaje_columna))
            if col >= 0 and col <= 2:                
                break
            else:
                print("La columna debe ser un valor entre 0-2")
        except:
            print("El valor que ingresaste para la columna no es valido")
    return fila, col