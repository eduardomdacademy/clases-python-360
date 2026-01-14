
# Función para imprimir el tablero
def imprimir_tablero_modo_1(tablero):
    for i,fila in enumerate(tablero):
        print(" | ".join(fila))
        if i < 2:
            print("--" * 5)

def imprimir_tablero_modo_2(tablero):
    for i,fila in enumerate(tablero):
        print(" || ".join(fila))
        if i < 2:
            print("==" * 6)