#cuando tratamos de acceder a un elemento de la lista a traves de su indice
#puede producirse un error si el indice esta fuera de rango

lista = ["rojo","amarillo","verde","celeste"]
print(lista[4])

#arroja un error porque el indice 4 esta fuera de rango
#el rango de los indices de una lista sera siempre 0 (el primero) hasta len(lista)-1 (cantidad de elementos menos uno)