with open("clase13\\asistencia.csv","r") as archivo:
    linea = archivo.readline()
    while len(linea) > 0:
        print(linea)
        linea = archivo.readline()