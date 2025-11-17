ingreso_valor_correcto = False
while not ingreso_valor_correcto: # va a continuar hasta que ingreso_valor_correcto sea True
    valor = input("Ingrese un valor entre 0 y 100: ")
    if valor.isnumeric():
        valor_numero = int(valor)
        if valor_numero >= 0 and valor_numero <= 100:
            ingreso_valor_correcto = True #El valor es correcto entonces terminamos
        else:
            print("El valor debe estar entre 0 y 100")
    else:
        print("El valor debe ser un numero")