#Los operadores logicos nos permiten agrupar expresiones logicas (Comparaciones o variables booleanas)
#el resultado de una operacion logica sera un valor booleano (Verdadero o falso)

#para el operador and el resultado sera True si y solo si ambos lados son True
a = 1
b = 5
c = 5
resultado  = (a<b) and (b ==c)
print("(a<b) and (b ==c)", resultado)
resultado = (a < c) and (a ==b) # falso porque a no es igual a b
print("(a < c) and (a ==b)", resultado)

#para el operador or el resultado sera True siempre que al menos uno de los lados sea True
a = 1
b = 5
c = 5

resultado = (a < c) or (a ==b) # verdadero porque a es menor a c
print("(a < c) or (a ==b)", resultado)
resultado = (a ==c) or (b < c) #false porque a es diferente a c, y b no es menor a c
print("(a ==c) or (b < c)", resultado)

#para el operador not solo habra un operando y el resultado sera el opuesto del valor del operando

resultado = not (a==5) # verdadero porque a no es igual a 5
print("not (a==5)", resultado)