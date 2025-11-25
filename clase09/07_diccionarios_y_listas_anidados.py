diccionario = {
    "marca": "Suzuki",
    "modelo": "Maruti",
    "año": 2001,
    "pasajeros": ["Luis","Raul","Ana"] 
}

print(diccionario)

#para acceder a valores anidados podemos hacerlo paso a paso
pasointermedio =  diccionario["pasajeros"]
print(pasointermedio)
print(pasointermedio[0])

#pero tambien podemos usar varios corchetes consecutivos para acceder en un solo paso
valor = diccionario["pasajeros"][0]
print(valor)