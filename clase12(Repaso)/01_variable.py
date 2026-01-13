variableNumero = 1
variableTexto = "esto es un ejemplo"
variableBooleana = True
variableBooleana2 = False


#Lo comentarios dentro de nuestro no forman parte de nuestro programa
#pero podemos usarlos para dejar aclaraciones o isntrucciones para su uso

#A una variable le podemos volver a asignar un nuevo valor
variableNumero = 3

#A una variable le puedo asignar el valor de una segunda variable
variableTexto2 = variableTexto

#Si yo el numero 1 quiero convertir al texto "1" puedo utilizar una funcion de casting

variableTexto = str(123) #el valor de variable texto sera el texto "123"
variableNumero = int("123")#el valor de la variableNumero sera el numero 123

#OBSERVACION: para el caso de texto a numeros facilmente podemos genera un errror porque un texto no necesariamente
#va a poder convertirse a numero
variableTexto = "Hola"
if variableTexto.isnumeric():
    variableNumero = int(variableTexto)


variableFloat = 0.345
print(variableFloat)