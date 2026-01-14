# Este es un juego de ta-te-ti
# falta implementar la funcion verificar_estado
# esta funcion se llamara luego de cada turno, y debe analizar el tablero para determinar si 
# alguno de los jugadores gano la partida
# un jugador gana una partida de ta-te-ti si coloca su marca en 3 casillas de la misma fila, columna o diagonal.
# si el tablero no tiene casillas vacias pero ninguno de los jugadores ganó se debe devolver "Empate"
# Si ninguno de los jugadores ganó pero aun se puede seguir jugando devolver ""

from salida.imprimir_tablero import imprimir_tablero_modo_2 as imprimir_tablero
import salida.entrada.pedir_jugada as pedir_jugada
import verificar_estado
 

def jugar():
    tablero = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]        
    ]
    jugador = "X"

    while True:
        imprimir_tablero(tablero)
        fila, col = pedir_jugada.pedir_jugada(jugador)

        if tablero[fila][col] == " ":
            tablero[fila][col] = jugador
        else:
            print("Casilla ocupada, intenta de nuevo.")
            continue

        estado = verificar_estado.verificar_estado(tablero)
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



