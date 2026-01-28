from tablero import Tablero
from pedir_jugada import pedir_jugada
from verificar_ganador import verificar_ganador
from chatgpt import pedi_jugada_chatgpt
def jugar():
    tablero = Tablero()
   
    jugador = "X"

    while True:
        tablero.imprimir()
        if jugador == "X":
            fila, col = pedir_jugada(jugador)
        else:
            fila, col = pedi_jugada_chatgpt(tablero)
        print(fila, col)        
        if tablero.leer_casilla(fila, col) == " ":
            tablero.marcar_casilla(fila, col, jugador)
        else:
            print("Casilla ocupada, intenta de nuevo.")
            continue

        estado = verificar_ganador(tablero)
        if estado != "":
            tablero.imprimir()
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



