def solicitar_valor_y_validarlo(valor_minimo, valor_maximo,mensaje):
    while True:
        texto_dia_seleccionado  = input(mensaje)
        if texto_dia_seleccionado.isnumeric():
            numero_seleccionado = int(texto_dia_seleccionado)
            if numero_seleccionado >= valor_minimo and numero_seleccionado <=valor_maximo:
                break
    return numero_seleccionado

dia = solicitar_valor_y_validarlo(1,31,"Ingrese un dia: ")
print("el dia", dia,"es valido")
mes = solicitar_valor_y_validarlo(1,12,"Ingresa un mes: ")
print("el mes", mes, "es valido")
anho = solicitar_valor_y_validarlo(1,2025,"Ingresa un anho: ")
print("el anho", anho, "es valido")
