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