#quiero imprimir solamente las ultimas 2 frutas
frutas = ["manzana","durazno", "naranja","frutilla"]

for posicion,fruta  in enumerate(frutas):
    if posicion >= len(frutas) - 2:
        print(posicion, fruta)
    
