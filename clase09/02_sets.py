set = {"banana", "pera", "frutilla"}
print(set)

#una vez creado el set podemos agregar nuevos valores utilizando el metodo 
set.add("sandia")
print("set luego de agregar",set)

#pero si tratamos de agregar un elemento que ya existia sera ignorado
set.add("pera")
print("luego de agregar un duplicado",set)

#para remover un elemento usamos el metodo remove
set.remove("frutilla")
print("luego de remover",set)
for fruta in set: #podemos iterar con un for...in
    print(fruta)

#los sets son muy utiles para almacenar valores y luego verificar si un 
#valor especifico ya se encuentra dentro del set.
if "pera" in set:
    print("el valor pera se encuentra dentro del set")

if "uva" in set:
    print("el valor uva esta en el set")
else:
    print("el valor uva no se encuentra en el set")

#Tambien podemos realizar las operaciones matematicas entre 2 sets:
#union, diferencia e interseccion
set1 = {"eduardo","maria"}
set2 = {"eduardo", "ana", "luis"}

union = set1.union(set2)
print("union", union)

diferencia = set1.difference(set2)
print("diferencia", diferencia)

interseccion= set1.intersection(set2)
print("interseccion", interseccion)

#Observacion NO podemos acceder a un elemento del set usando indicies
#set[0] arrojaria un error