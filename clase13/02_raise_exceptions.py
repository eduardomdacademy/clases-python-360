
lista = ["Eduardo Filippi", "Ana Lopez", "", "Luis Martinez"]
for nombre in lista:
    if len(nombre) == 0:
        raise Exception("el nombre no puede estar vacio")
    print(nombre)

