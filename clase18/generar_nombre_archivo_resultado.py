import os
def generar_nombre_archivo_resultado(carpeta):
    archivos = os.listdir(carpeta)
    numeros = []
    for archivo in archivos:
        nombre_y_tipo = archivo.split(".")
        nombre = nombre_y_tipo[0]
        numero = int(nombre.split("_")[1])
        numeros.append(numero)
    numeros.sort()
    if len(numeros) == 0:
        return "resultado_1.xlsx"
    mayor = numeros[len(numeros) - 1]
    numero = mayor + 1
    return "resultado_" + str(numero) + ".xlsx"

        
