import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from leer_excel import leer_excel
from pathlib import Path
from Cotizacion import Cotizacion
from sklearn import linear_model

path_archivo = Path("clase19") / "resultados" / "resultado.xlsx"
cotizaciones = leer_excel(path_archivo)
fechas = []
compras = []
ventas = []
numeros = []
puntos_compras = []
numero = 1
for cotizacion in cotizaciones:
    cotizacion:Cotizacion
    numeros.append([numero])
    puntos_compras.append(cotizacion.compra)
    fechas.append(cotizacion.fecha)
    compras.append(cotizacion.compra)
    ventas.append(cotizacion.venta)
    numero += 1

fig, ax = plt.subplots()       
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=np.arange(1, 13, 1)))

ax.plot(fechas, compras)  
ax.plot(fechas, ventas)

reg = linear_model.LinearRegression()


reg.fit(numeros,puntos_compras)
fechas_proyeccion = []
valor_proyecion = []
for i in range(0,len(fechas)):
    fechas_proyeccion.append(fechas[i])
    valor = reg.intercept_  + (i*reg.coef_)  
    valor_proyecion.append(valor)
    
for i in range(0,10):
    fechas_proyeccion.append("2026-02-0" + str(i))
    valor_proyecion.append(reg.intercept_  + ((len(fechas)+i)*reg.coef_))

print("coef_",reg.coef_)
print("intercept",reg.intercept_)
ax.plot(fechas_proyeccion, valor_proyecion)  



plt.xlabel("Fecha")
plt.ylabel("Costo Guaranies")

plt.show() 