# Ejercicio 1
# Para la siguiente lista de palabras
# palabras = ["python", "java", "python", "c", "java", "python"]
# Crea un nuevo programa que calcule cuantas veces se repite cada palabra
# Y genere una nueva lista donde cada elemento será un diccionario
# Con dos claves 
# •	Palabra: la palabra de la lista original
# •	Repeticiones: cuantas veces aparece esa palabra en la lista original
# Ejemplo:
# {
# “palabra”:”python”
# “repeticiones”:3
# }
# Imprimir la palabra con mayor numero de repeticiones y cuantas veces se repitió
#
palabras = ["java","python", "python", "Luis", "c", "java","Luis", "python", "Luis","Luis"]
lista_resultados= [] #variable para almacenar el resultado
for palabra in palabras:
    bandera_palabra_nueva = True
    for palabra_ya_guardada in lista_resultados:
        if palabra == palabra_ya_guardada["palabra"]: #Si ya habiamos encontrado anteriormente esta palabra
            bandera_palabra_nueva = False
            palabra_ya_guardada["repeticiones"] += 1
    if bandera_palabra_nueva: #Si es la primera vez que encontramos esta palabra
        contador = {
            "palabra":palabra,
            "repeticiones" : 1
        }
        lista_resultados.append(contador)

print(lista_resultados)

cantidad_mas_alta = -1 #Elijo -1 como valor inicia para que el primer valor de la lista siempre sea Mayor
palabra_con_mas_cantidad = ""
for diccionario in lista_resultados:
    if diccionario["repeticiones"] > cantidad_mas_alta: 
        cantidad_mas_alta = diccionario["repeticiones"]
        palabra_con_mas_cantidad = diccionario["palabra"]

print("La palabra que mas se repite es:", palabra_con_mas_cantidad)
print("y se repite",cantidad_mas_alta,"veces")
