for numero in range(10,51):
    es_primo = True
    for i in range(2,numero):
        if numero%i==0:
            print("El numero es divisible por ", i)
            print("el numero no es primo")
            es_primo = False
            break
        print("El numero NO es divisible por ", i)

    if es_primo == True:
        mensaje = "El numero " + str(numero) + " es primo"
        print(mensaje)