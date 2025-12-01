fila1 = [" ", " ", " "]
fila2 = [" ", " ", " "]
fila3 = [" ", " ", " "]
tablero = [fila1, fila2, fila3]

fila = input("Ingrese la fila: ")
fila_numero = int(fila)
columna = input("Ingrese la columna: " )
columna_numero = int(columna)
tablero[fila_numero][columna_numero] = "X"

print(tablero)
for numero_fila, fila in enumerate(tablero):
    mensaje = fila[0] + " | " + fila[1] + " | " + fila[2]
    print(mensaje)
    if numero_fila < 2:
        print("_________")
            