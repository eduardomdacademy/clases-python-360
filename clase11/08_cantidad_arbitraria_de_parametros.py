def promedio_de_puntajes(nombre,apellido, *notas):
    # print(notas)
    if len(notas) == 0:
        print("ERROR: la cantidad de notas no puede ser 0")
        return
    suma = 0
    for nota in notas:
        suma += nota
    promedio = suma / len(notas)
    print("el promedio de", nombre, apellido, "es:", promedio)

promedio_de_puntajes("Luis", "lopez", 70)
promedio_de_puntajes("Ana", "martinez", 80,80, 100, 90, 100)
