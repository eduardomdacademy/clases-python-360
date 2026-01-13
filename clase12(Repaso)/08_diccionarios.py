diccionario = {
    "numero_de_cedula" : 5555555,
    "nombre": "Eduardo",
    "apellido": "Filippi",
    "Fecha de nacimiento":{
        "dia": "28",
        "mes":"11",
        "año":"1990"
    },
    "Estado civil": "casado",
    "Hijos": ["Lucia","Maria","Jose"]
}

print(diccionario["apellido"])
diccionario["nombre"] = "Luis"
print(diccionario)

diaDeNacimiento = diccionario["Fecha de nacimiento"]["dia"]
print(diaDeNacimiento)