# Ejercicio 2
# Utilizando la siguiente lista de diccionarios
# estudiantes = [
#     {
#         "nombre": "Ana",
#         "notas": [85, 90, 78]
#     },
#     {
#         "nombre": "Luis",
#         "notas": [70, 88, 95]
#     },
#     {
#         "nombre": "María",
#         "notas": [92, 81, 85]
#     },
#     {
#         "nombre": "Carlos",
#         "notas": [60, 75, 72]
#     },
#     {
#         "nombre": "Sofía",
#         "notas": [100, 95, 98]
#     }
# ]
# Crear un programa que para cada estudiante calcule el promedio de sus notas e imprima el nombre del estudiante que tenga el promedio más alto y cual fue su promedio.

estudiantes = [
    {
        "nombre": "Ana",
        "notas": [85, 90, 78]
    },
    {
        "nombre": "Luis",
        "notas": [70, 88, 95]
    },
    {
        "nombre": "María",
        "notas": [92, 81, 85]
    },
    {
        "nombre": "Carlos",
        "notas": [60, 75, 72]
    },
    {
        "nombre": "Sofía",
        "notas": [100, 95, 98]
    }
]
promedio_mas_alto = -1
estudiante_con_mayor_promedio = ""
for estudiante in estudiantes:
    notas = estudiante["notas"]
    acumulador = 0
    for nota in notas:
        acumulador += nota
    promedio = acumulador/len(notas)
    if promedio > promedio_mas_alto:
        promedio_mas_alto = promedio
        estudiante_con_mayor_promedio = estudiante["nombre"]
mensaje = "El estudiante con mayor promedio es " + estudiante["nombre"] + " con un promedio de " + str(promedio_mas_alto)
print(mensaje)