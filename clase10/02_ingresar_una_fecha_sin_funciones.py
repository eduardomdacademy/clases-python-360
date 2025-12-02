#Queremos soliciatar al usuario que ingrese una fecha
#primero le pediremos que ingrese un dia entre 1 y 31
#luego le pediremos que ingrese un mes entre 1 y 12
# luego le pediremos que ingrese un anho entre 1990 y 2025
while True:
    texto_dia_seleccionado  = input("Ingrese un numero:")
    if texto_dia_seleccionado.isnumeric():
        numero_dia_seleccionado = int(texto_dia_seleccionado)
        if numero_dia_seleccionado >= 1 and numero_dia_seleccionado <=31:
            break
print("el numero ", numero_dia_seleccionado, "es valido")

while True:
    texto_mes_seleccionado = input("Ingrese el mes:")
    if texto_mes_seleccionado.isnumeric():
        numero_mes_seleccionado = int(texto_mes_seleccionado)
        if numero_mes_seleccionado >= 1 and numero_mes_seleccionado <= 12:
            break
print("el mes ", numero_mes_seleccionado, "es valido")

while True:
    texto_anho_seleccionado = input("Ingrese el anho:")
    if texto_mes_seleccionado.isnumeric():
        numero_anho_seleccionado = int(texto_anho_seleccionado)
        if numero_anho_seleccionado > 0 and numero_anho_seleccionado <= 2025:
            break
print("el anho", numero_anho_seleccionado, " es valido" )