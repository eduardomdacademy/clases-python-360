def imprimir_familia(nombre_padre, apellido_padre,nombre_madre, apellido_madre, *hijos):
    print("Padre:", nombre_padre, apellido_padre)
    print("Madre:", nombre_madre, apellido_madre)
    print(hijos)
    for indice in range(0,len(hijos),2):
        nombre = hijos[indice]
        apellido = hijos[indice+1]
        print("Hijo: ", nombre, apellido)
imprimir_familia("Luis", "Lopez", "Maria", "Benitez", "Raul", "Lopez", "Ana", "Lopez", "Lucia","Lopez")