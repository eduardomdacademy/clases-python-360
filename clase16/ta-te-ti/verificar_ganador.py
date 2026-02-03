
from tablero import Tablero

def verificar_ganador(tablero: Tablero):
    #Fila1
    if _son_iguales(tablero.leer_casilla(0,0),tablero.leer_casilla(0,1), tablero.leer_casilla(0,2)):
        if tablero.leer_casilla(0,0) == "X":
            return "X"
        elif tablero.leer_casilla(0,0) == "O":
            return "O"
    #Fila2
    if _son_iguales(tablero.leer_casilla(1,0),tablero.leer_casilla(1,1), tablero.leer_casilla(1,2)):
        if tablero.leer_casilla(1,0) == "X":
            return "X"
        elif tablero.leer_casilla(1,0) == "O":
            return "O"
    #Fila3
    if _son_iguales(tablero.leer_casilla(2,0),tablero.leer_casilla(2,1), tablero.leer_casilla(2,2)):
        if tablero.leer_casilla(2,0) == "X":
            return "X"
        elif tablero.leer_casilla(2,0) == "O":
            return "O"
    #columna1
    if _son_iguales(tablero.leer_casilla(0,0),tablero.leer_casilla(1,0), tablero.leer_casilla(2,0)):
        if tablero.leer_casilla(0,0) == "X":
            return "X"
        elif tablero.leer_casilla(0,0) == "O":
            return "O"
    #columna2
    if _son_iguales(tablero.leer_casilla(0,1),tablero.leer_casilla(1,1), tablero.leer_casilla(2,1)):
        if tablero.leer_casilla(0,1) == "X":
            return "X"
        elif tablero.leer_casilla(0,1) == "O":
            return "O"
    #columna3
    if _son_iguales(tablero.leer_casilla(0,2),tablero.leer_casilla(1,2), tablero.leer_casilla(2,2)):
        if tablero.leer_casilla(0,2) == "X":
            return "X"
        elif tablero.leer_casilla(0,2) == "O":
            return "O"
    #Diagonal principal
    if _son_iguales(tablero.leer_casilla(0,0),tablero.leer_casilla(1,1), tablero.leer_casilla(2,2)):
        if tablero.leer_casilla(0,0) == "X":
            return "X"
        elif tablero.leer_casilla(0,0) == "O":
            return "O"
    #Diagonal segundaria
    if _son_iguales(tablero.leer_casilla(2,0),tablero.leer_casilla(1,1), tablero.leer_casilla(0,2)):
        if tablero.leer_casilla(2,0) == "X":
            return "X"
        elif tablero.leer_casilla(2,0) == "O":
            return "O"
    #Si nadie gano, comprobamos que quede al menos 1 espacio libre
    #osino se acaba en empate 
    
    if tablero.hay_por_lo_menos_un_espacio_vacio():        
        return "" 
    else:
        return "Empate"



def _son_iguales(valor1, valor2, valor3):
    if valor1 == valor2:
        if valor2 == valor3:
            return True
    return False
