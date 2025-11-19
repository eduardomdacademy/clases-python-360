#imprimir todas las frutas excepto la sandia

frutas = ["manzana","durazno", "sandia", "naranja","frutilla"]
for fruta in frutas:
    if fruta == "sandia":
        continue
    print(fruta)
