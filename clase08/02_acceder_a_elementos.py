#Nosotros podemos acceder a un elemento de la lista a traves de su indice

lista = ["banana", "frutilla", "banana", "pera"]

print("lista",lista)
print("lista[0]",lista[0])
print("lista[1]",lista[1])

#pero tambien podemos usar indice negativo, para contar elementos desde el final

print("lista[-1]",lista[-1]) #el ultimo elemento
print("lista[-3]", lista[-3])#el tercer elemento contando desde el final

#Tambien podemos acceder a la lista usando rangos
#cuando usamos un rango obtenemos una nueva lista con los elementos seleccionados

lista2 = lista[1:3]
print("lista[1:3]", lista2) #elementos tomados a partir del segundo (indice 1) hasta el cuarto (excluyente)

lista3 = lista[:2]
print("lista[:2]",lista3) #si dejamos vacio el primer valor tomara desde el primer elemento hasta el limite indicado

lista4 =lista[1:]
print("lista[1:]", lista4)#si dejamos vacio el segundo valor tomara desde el indice indicado hasta el ultimo elemento.

lista5 = lista[:]
print("lista[:]", lista5) #si dejamos vacios ambos seran todos los elementos de la lista, lo cual no es particularmente util
