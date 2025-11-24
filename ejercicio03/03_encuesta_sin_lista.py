comidas_favoritas = ""
cantidad = 0
while True:
    #cantidad += 1
    comida = input("Ingresa una comida favorita: ")
    comida_minusculas = comida.lower()
    if comida_minusculas == "salir":
        break
    cantidad += 1

    if cantidad == 1: #es la primera vez
        comidas_favoritas = comidas_favoritas + comida
    else:
        comidas_favoritas = comidas_favoritas + ", " + comida
    

mensaje_cantidad = "Se ingresaron " + str(cantidad) + " comidas"
print(mensaje_cantidad)
print(comidas_favoritas)
