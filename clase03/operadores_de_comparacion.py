x = 4
resultado = (x == 4)
print("primera comparacion",str(resultado))
x += 2
resultado = (x == 4)
print("segunda comparacion",str(resultado))
y=6
resultado = (x == y)
print("tercera comparacion",str(resultado))

x = 2
y = 5
igualdad = (x == y)
diferente = (x != y)
print("igualdad",igualdad)
print("diferente",diferente)


menor = (8 < 8) #falso
menor_o_igual = (8 <= 8) #verdadero
print("menor", menor)
print("menor_o_igual", menor_o_igual)