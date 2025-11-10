texto = "Hola Mundo"
textoEnMayusculas = texto.upper()
print(textoEnMayusculas)

textoEnMinusculas = texto.lower()
print(textoEnMinusculas)

texto_reemplazado = textoEnMinusculas.replace("mundo","planeta tierra")
print(texto_reemplazado)

#el metodo split separa el texto segun un separador
texto_a_separar = "Esta es la primera oracion|la segunda oracion|tercera."
texto_separado = texto_a_separar.split("|")
print(texto_separado)

texto_con_espacios = "   Este texto tiene espacios extras    "
print(texto_con_espacios)
texto_sin_espacios = texto_con_espacios.strip()
print(texto_sin_espacios)
print(texto_con_espacios)

#Existen varios metodos que nos permiten hacer preguntas sobre nuestro texto
texto = "La banana es una fruto"
resultado = texto.find("banana")
print("texto.find(\"banana\")", resultado)
resultado = texto.find("frutilla")
print("texto.find(\"frutilla\")", resultado)
resultado = texto.startswith("La bana")
print("texto.startswith(\"La bana\")", resultado)
