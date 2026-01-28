class Tablero:
    def __init__(self):
        self.__tablero = [
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]        
            ]
    
    def imprimir(self):
        for i,fila in enumerate(self.__tablero):
            print(" | ".join(fila))
            if i < 2:
                print("--" * 5)
                
    def generar_texto_tablero(self):
        texto = ""
        for i,fila in enumerate(self.__tablero):
            texto +=" | ".join(fila) + "\n"
            if i < 2:
                texto += "--" * 5 + "\n"
        return texto
    def leer_casilla(self, fila, col):
        return self.__tablero[fila][col]
    
    def marcar_casilla(self,fila, col, marca):
        self.__tablero[fila][col] = marca

    def hay_por_lo_menos_un_espacio_vacio(self):
        for fila in self.__tablero:
            for casilla in fila:
                if casilla == " ":
                    return True
        return False