#Los diccionarios nos permiten agrupar valores dentro de una misma variable
#con la intencion de que esos valores queden asociados como parte de una misma entidad
persona = {
    "nombre": "Eduardo",
    "apellido": "Filippi",
    "edad": 21,
    "estado_civil": "Casado",
    "tiene_trabajo": True,
}
print(persona)

persona2 = {
    "nombre": "Luis",
    "apellido": "Riquelme",
    "edad": 30,
    "estado_civil": "Soltero",
    "tiene_trabajo": False,
}
print(persona2)

print("el nombre de la persona1 es: ",persona["nombre"])
print("el nombre de la persona2 es: ",persona2["nombre"])

#Para modificiar un valor usamos corchetes y la clave que deseamos modificar
persona2["nombre"] = "Raquel"
print("el nombre de la persona 2 luego de modificar es: ", persona2["nombre"])

#si tratamos de asignar un valor a una clave que aun no existe, se agregara esta clave al diccionario
persona2["profesion"] = "Estudiante"
print("persona2 luego de agregar profesion", persona2)

#tambien podemos iterar entre todos los valores de un diccionario, pero esto no es particularmente util
for clave in persona:
    print("clave:",clave,"valor:",persona[clave])

