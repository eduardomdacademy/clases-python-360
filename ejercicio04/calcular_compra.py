# Ejercicio Bonus
# Utilizando la siguiente lista de diccionarios
# inventario = {
#     "manzanas": {"precio": 2, "stock": 10},
#     "naranjas": {"precio": 3, "stock": 5},
#     "bananas": {"precio": 1.5, "stock": 8}
# }
# •	Solicitar al usuario que ingrese el nombre de una fruta.
# o	Si no está en la lista mostrar un mensaje de error y terminar
# •	Solicitar al usuario que ingrese la cantidad que desea
# o	Si la cantidad es mayor al stock mostrar un error
# •	Mostrar en pantalla cual será el precio total (cantidad * precio)
# •	Descontar del stock de la fruta correspondiente la cantidad elegida

inventario = {
    "manzanas": {"precio": 2, "stock": 10},
    "naranjas": {"precio": 3, "stock": 5},
    "bananas": {"precio": 1.5, "stock": 8}
}
while True:
    fruta_elegida = input("Ingrese un producto:")
    if not fruta_elegida in inventario:
        print("La fruta no está en el inventario")
    else:
        break

while True:
    cantidad_elegida = input("Ingrese la cantidad: ")
    cantidad_elegida_numero = int(cantidad_elegida)
    if cantidad_elegida_numero > inventario[fruta_elegida]["stock"]:
        print("El stock de la fruta seleccionada es solamente", inventario[fruta_elegida]["stock"])
    else:
        break

precio_total = cantidad_elegida_numero * inventario[fruta_elegida]["precio"]
inventario[fruta_elegida]["stock"] -= cantidad_elegida_numero

mensaje = "El precio total de la compra sera " + str(precio_total) + "\nY quedan " + str(inventario[fruta_elegida]["stock"]) + " " + fruta_elegida + " en stock."
print(mensaje)