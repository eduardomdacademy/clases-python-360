import os
from leer_excel import leer_excel
from pathlib import Path
from cotizacion import Cotizacion


def leer_carpeta(carpeta):
    archivos = os.listdir(carpeta)
    resultado = []
    for archivo in archivos:
        if archivo[0] == "~":
            continue
        path = Path(carpeta) / archivo
        print(path)
        lista_cotizacion = leer_excel(path)
        resultado = resultado + lista_cotizacion
    return resultado


