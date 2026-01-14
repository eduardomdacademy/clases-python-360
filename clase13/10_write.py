with open("clase13\\asistencia.csv","r") as archivo:
    with open("clase13\\resultado.txt","a") as resultado:
        linea = archivo.readline()
        while len(linea) > 0:
            resultado.write(linea)
            linea = archivo.readline()