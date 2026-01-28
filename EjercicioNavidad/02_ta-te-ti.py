# Este es un juego de ta-te-ti
# falta implementar la funcion verificar_estado
# esta funcion se llamara luego de cada turno, y debe analizar el tablero para determinar si 
# alguno de los jugadores gano la partida
# un jugador gana una partida de ta-te-ti si coloca su marca en 3 casillas de la misma fila, columna o diagonal.
# si el tablero no tiene casillas vacias pero ninguno de los jugadores ganó se debe devolver "Empate"
# Si ninguno de los jugadores ganó pero aun se puede seguir jugando devolver ""

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for i,fila in enumerate(tablero):
        print(" | ".join(fila))
        if i < 2:
            print("--" * 5)

# Función para recibir input del jugador
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

#Función que el estudiante debe implementar
def verificar_estado(tablero):
# Debe devolver:
# - 'X' si el jugador X ganó
# - 'O' si el jugador O ganó
# - 'Empate' si no hay más espacios y nadie ganó
# -  "" si la partida sigue
    #Fila1
    if _son_iguales(tablero[0][0],tablero[0][1], tablero[0][2]):
        if tablero[0][0] == "X":
            return "X"
        elif tablero[0][0] == "O":
            return "O"
    #Fila2
    if _son_iguales(tablero[1][0],tablero[1][1],tablero[1][2]):
        if tablero[1][0] == "X":
            return "X"
        elif tablero[1][0] == "O":
            return "O"
    #Fila3
    if _son_iguales(tablero[2][0],tablero[2][1],tablero[2][2]):
        if tablero[2][0] == "X":
            return "X"
        elif tablero[2][0] == "O":
            return "O"
    #columna1
    if _son_iguales(tablero[0][0], tablero[1][0], tablero[2][0]):
        if tablero[0][0] == "X":
            return "X"
        elif tablero[0][0] == "O":
            return "O"
    #columna2
    if _son_iguales(tablero[0][1], tablero[1][1], tablero[2][1]):
        if tablero[0][1] == "X":
            return "X"
        elif tablero[0][1] == "O":
            return "O"
    #columna3
    if _son_iguales(tablero[0][2], tablero[1][2], tablero[2][2]):
        if tablero[0][2] == "X":
            return "X"
        elif tablero[0][2] == "O":
            return "O"
    #Diagonal principal
    if _son_iguales(tablero[0][0], tablero[1][1], tablero[2][2]):
        if tablero[0][0] == "X":
            return "X"
        elif tablero[0][0] == "O":
            return "O"
    #Diagonal segundaria
    if _son_iguales(tablero[2][0], tablero[1][1], tablero[0][2]):
        if tablero[2][0] == "X":
            return "X"
        elif tablero[2][0] == "O":
            return "O"
    #Si nadie gano, comprobamos que quede al menos 1 espacio libre
    #osino se acaba en empate
    espacio_vacio_encontrado = False
    for fila in tablero:
        for casilla in fila:
            if casilla == " ":
                espacio_vacio_encontrado = True
    if espacio_vacio_encontrado:        
        return "" 
    else:
        return "Empate"



def _son_iguales(valor1, valor2, valor3):
    if valor1 == valor2:
        if valor2 == valor3:
            return True
    return False
# Programa principal
def jugar():
    tablero = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]        
    ]
   
    jugador = "X"

    while True:
        imprimir_tablero(tablero)
        fila, col = pedir_jugada(jugador)
        if tablero[fila][col] == " ":
            tablero[fila][col] = jugador
        else:
            print("Casilla ocupada, intenta de nuevo.")
            continue

        estado = verificar_estado(tablero)
        if estado != "":
            imprimir_tablero(tablero)
            if estado == "Empate":
                print("La partida fue un empate")
            else:
                print("El ganador es el jugador ", estado)
            break

        # Cambiar de jugador
        if jugador == "X":
            jugador = "O"
        else:
            jugador = "X"

jugar()



