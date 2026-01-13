# Este programa lee el archivo asistencia.csv que debe estar en la misma carpeta que el script
# se debe implementar la funcion calcular asistencia
#Observacion para que se lea correctamente quizas haga falta cambiar la ruta al archivo csv
import csv

# Función para leer el archivo CSV
def leer_csv(nombre_archivo):
    estudiantes = []
    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        lector = csv.reader(f)
        encabezado = next(lector)  # saltar la primera fila
        for fila in lector:
            nombre = fila[0]
            asistencias = list(map(int, fila[1:]))
            estudiantes.append((nombre, asistencias))
    return estudiantes

#Función que el alumno debe implementar
def calcular_asistencia(asistencias):    
    # Recibe una lista de 0s y 1s.
    #1 significa que el alumno estuvo presente esa clase
    #0 significa que el alumno estuvo ausente esa clase
    # Debe devolver True si el estudiante alcanzó al menos el 70% de asistencia,
    # False en caso contrario.   
    total_clases = len(asistencias)
    cantidad_de_presentes = 0
    for asistencia in asistencias:
        if asistencia == 1:
            cantidad_de_presentes += 1
    porcentaje = (cantidad_de_presentes/total_clases) *100
    print(porcentaje)
    if porcentaje >= 70:
        return True
    else:
        return False
    
#OBSERVACION
#esta ruta al archivo prodria hacer falta ajustar
#se puede hacer segundo click sobre el archivo en el explorador de la izquierda y seleccionar la opcion "Copiar ruta de acceso relativa"
#recuerda escapar los \ usando \\
ruta_archivo = "EjercicioNavidad\\asistencia.csv"

estudiantes = leer_csv(ruta_archivo)
for nombre, asistencias in estudiantes:
    if calcular_asistencia(asistencias):        
        print(nombre,"alcanzó el 70% de asistencia")
    else:
        print(nombre,"NO alcanzó el 70% de asistencia")

