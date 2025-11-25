lista = ["rojo", "blanco", "azul", "verde"]
print("lista antes de remove", lista)
lista.remove("blanco")
print("lista luego de remover", lista)

#remove solo remueve el PRIMER elemento con el valor dado
lista = ["rojo", "blanco","azul", "verde", "blanco", "amarillo"]
print("lista con duplicados", lista)
lista.remove("blanco")
print("Solo se removio el primero", lista)