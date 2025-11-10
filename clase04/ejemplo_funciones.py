#Queremos perdir al usuario un texto, 
# luego queres pedir un texto a buscar dentro del primer texto, 
# luego pedimos al usuario un tercer texto que vamos a reemplazar en primero en vez del segundo texto
#convertir los dos primero textos en minusculas para evitar que no distinga mayusculas de minusculas
texto_ingresado = input("Por favor ingresa un texto: ")
texto_para_buscar = input("Ingresa el texto a buscar:")
texto_para_reemplazar = input("Ingresa el texto a reemplazar: ")
texto_ingresado_minuscula = texto_ingresado.lower()
texto_para_buscar_minuscula = texto_para_buscar.lower()
resultado = texto_ingresado_minuscula.replace(texto_para_buscar_minuscula, texto_para_reemplazar)
mensaje = "El texto final es: " + resultado
print(mensaje)

