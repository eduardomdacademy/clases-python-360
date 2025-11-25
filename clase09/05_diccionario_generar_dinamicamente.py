diccionario = {}
while True:
    clave = input("ingresa la clave: ")
    if clave == "salir":
        break
    valor= input("ingresa el valor: ")
    diccionario[clave] = valor

print(diccionario)
