a = input("ingresa el primer valor: ")
b = input("ingresa el segundo valor: ")
if len(a) < len(b):
    print("el primer valor es mas corto que el segundo")
elif len(a) > len(b):
    print("el primer valor es mas largo que el segundo")
elif len(a) == len(b):
    print("el primer valor es igual de largo que el segundo")
print("esta linea ya está fuera del if")    