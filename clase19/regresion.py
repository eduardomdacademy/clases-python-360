from sklearn import linear_model

def calcular_regresion(ax, numeros, puntos, fechas, nombre):
    reg = linear_model.LinearRegression()
    reg.fit(numeros, puntos)
    fechas_proyeccion = []
    valor_proyeccion = []
    for i in range(0, len(fechas)):
        fechas_proyeccion.append(fechas[i])
        valor = reg.intercept_ + (i * reg.coef_)
        valor_proyeccion.append(valor)
    for i in range(0, 10):
        fechas_proyeccion.append("2026-02-0" + str(i))
        valor_proyeccion.append(reg.intercept_ + ((len(fechas) + i) * reg.coef_))
    print(nombre, "coef_", reg.coef_)
    print(nombre, "intercept", reg.intercept_)
    ax.plot(fechas_proyeccion, valor_proyeccion)
