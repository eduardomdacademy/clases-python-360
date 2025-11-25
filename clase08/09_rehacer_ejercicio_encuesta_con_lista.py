comidas_favoritas = []
while True:
    comida = input("Ingresa una comida favorita: ")
    comida_minusculas = comida.lower()
    if comida_minusculas == "salir":
        break
    comidas_favoritas.append(comida)

mensaje = ""
primera_vez = True
for comida in comidas_favoritas:
    if primera_vez == True:
        mensaje = mensaje + comida
        primera_vez = False
    else:
        mensaje = mensaje + ", " + comida
cantidad = len(comidas_favoritas)
mensaje_cantidad = "Se ingresaron " + str(cantidad) + " comidas"
print(mensaje_cantidad)
print(mensaje)