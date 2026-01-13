colores = ["rojo","blanco","azul"]
colores.append("purpura")

for color in colores:
    print(color)

for indice, color in enumerate(colores):
    colores[indice] = color.upper()

print(colores)
   
