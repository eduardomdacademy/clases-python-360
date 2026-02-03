from generar_nombre_archivo_resultado import generar_nombre_archivo_resultado
from leer_carpeta import leer_carpeta
from pathlib import Path
from cotizacion import Cotizacion
from guardar_cotizaciones import guardar_resultados
path_carpeta = Path("clase18")/"cotizacion"

cotizaciones = leer_carpeta(path_carpeta)



path_carpeta_resultados = Path("clase18")/"resultados"
nombre_archivo_resultado = generar_nombre_archivo_resultado(path_carpeta_resultados)
path_archivo_resultado  = path_carpeta_resultados / nombre_archivo_resultado
guardar_resultados(cotizaciones, path_archivo_resultado)

