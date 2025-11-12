a = input("ingresa un valor: ")
if len(a) == 0:
    print("El valor esta vacio")
elif len(a) < 5:
    print("El largo del valor es menor a 5")
elif len(a) < 10:
    print("El largo del valor es mayor o igual a 5 pero menor a 10")
else:
    print("el largo del valor es mayor o igual a 10")
print("esta linea ya está fuera del if")