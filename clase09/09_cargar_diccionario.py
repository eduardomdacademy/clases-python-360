alumnos = []
while True: 
    nombre = input("ingresa el nombre: ")
    apellido = input("ingresa el apellido: ")
    alumno = {}
    alumno["nombre"] = nombre
    alumno["apellido"] = apellido
    notas = []
    while True:
        nota = input("ingresa una nota para este alumno: ")
        if nota == "salir":
            break
        notas.append(nota)
    alumno["notas"] = notas    
    alumnos.append(alumno)
    eleccion = input("Deseas continuar? s/n: ")
    if eleccion != "s":
        break;
print("---------------------------------")
for alumno in alumnos:    
    print("nombre=",alumno["nombre"])
    print("apellido=",alumno["apellido"])
    print("notas=",alumno["notas"])
    print("---------------------------------")