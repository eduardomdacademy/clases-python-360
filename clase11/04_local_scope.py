def operaciones(valor1, valor2):
    suma = valor1 + valor2
    resta = valor1 - valor2
    division = valor1 / valor2
    multiplicacion = valor1 * valor2
    return {
        "multiplicacion": multiplicacion, 
        "suma":suma, 
        "resta":resta,
        "division":division
    }


resultado = operaciones(2,6)
suma = resultado["suma"]
resta = resultado["resta"]
multiplicacion = resultado["multiplicacion"]
print(suma, resta, multiplicacion)