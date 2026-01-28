#Teniendo en el archivo emails.txt la lista de emails de nuestros clientes
#Escribir un script que lea esa lista y cuente cuantos clientes utilizan cada dominio de email diferente
#Los dominios seria la segunda parte del mail, luego del @
import email

dominios = {}
with open("clase16/emails/emails.txt") as f:
    linea = f.readline()
    while len(linea) > 0:  
        variableEmail = email.Email(linea)
        dominio = variableEmail.obtener_dominio()
        if dominio in dominios:
            dominios[dominio] += 1
        else:
            dominios[dominio] = 1

        linea = f.readline()
for llave in dominios:
    print("El dominio", llave, "aparece", dominios[llave],"veces")
