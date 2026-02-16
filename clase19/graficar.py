import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from leer_excel import leer_excel
from pathlib import Path
from Cotizacion import Cotizacion
from regresion import calcular_regresion

path_archivo = Path("clase19") / "resultados" / "resultado.xlsx"
cotizaciones = leer_excel(path_archivo)
fechas = []
compras = []
ventas = []
numeros = []
puntos_compras = []
puntos_ventas = []
numero = 1
for cotizacion in cotizaciones:
    cotizacion:Cotizacion
    numeros.append([numero])
    puntos_compras.append(cotizacion.compra)
    puntos_ventas.append(cotizacion.venta)
    fechas.append(cotizacion.fecha)
    compras.append(cotizacion.compra)
    ventas.append(cotizacion.venta)
    numero += 1

fig, ax = plt.subplots()
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=np.arange(1, 13, 1)))

ax.plot(fechas, compras)
ax.plot(fechas, ventas)

calcular_regresion(ax, numeros, puntos_compras, fechas, "Compra")
calcular_regresion(ax, numeros, puntos_ventas, fechas, "Venta")

plt.xlabel("Fecha")
plt.ylabel("Costo Guaranies")

plt.show()
