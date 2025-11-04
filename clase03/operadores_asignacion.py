#colocamos una variable a la izquierda del operador = y a la derecha un valor
#y ese valor queda guardado dentro de la variable
x = 5
print("primera asignacion de x=",x)
#podemos volver a asignar a la misma variable y el valor se sobreescribe
x  = "Hola mundo"
print("x luego de sobreescribir =",x)
x = 20
print("valor antes de incrementar",x)
x += 27 #Esto es exactamente igual a x = x + 1
print("valor despues de incrementar",x)

y = 10
print("valor antes de decrementar",y)
y -= 7
print("valor despues de decrementar",y)