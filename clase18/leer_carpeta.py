import os
from leer_excel import leer_excel
from pathlib import Path
from cotizacion import Cotizacion


def leer_carpeta(carpeta):
    archivos = os.listdir(carpeta)

    resultados = []
    for archivo in archivos:
        if archivo[0] == "~":
            continue
        path = Path(carpeta) / archivo
        print(path)
        lista_cotizacion = leer_excel(path)
        resultados = resultados + lista_cotizacion
    return resultados


