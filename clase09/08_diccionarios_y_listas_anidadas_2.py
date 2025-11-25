alumnos = [
    {
        "nombre":"Eduardo",
        "apellido": "Filippi",
        "edad":21,
        "direccion": {
            "calle": "Mariscal Lopez",
            "calle_secundaria": "Republica Argentina",
            "numero de casa": 555,            
        }
    },
    {
        "nombre":"Jose",
        "apellido": "Lopez",
        "edad":30,
        "direccion": {
            "calle": "Eusebio Ayala",
            "calle_secundaria": "Madame Lynch",
            "numero de casa": 22222,
        }
    }
]
print(alumnos)

#imprimir las calles en las que vive el primer alumno
calle = alumnos[0]["direccion"]["calle"]
print(calle)
#imprimir todas las calles en las que viven los alumnos
for alumno in alumnos:
    print(alumno["direccion"]["calle"])