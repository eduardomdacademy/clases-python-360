# Ejercicio 2:
# Escribe un programa que solicite al usuario:
# •	Su año de nacimiento
# •	El numero de mes de su nacimiento (1-12)
# •	Su día del mes de nacimiento
# •	El año actual
# •	El numero de mes actual (1-12)
# •	El día del mes actual 
# Y a partir de estos datos determine cuantos años tiene actualmente e imprima la respuesta


anho_nacimiento_string = input("Ingresa tu año de nacimiento: ")
if anho_nacimiento_string.isnumeric():
    anho_nacimiento_numero = int(anho_nacimiento_string)
    mes_nacimiento_string = input("Ingresa tu mes de nacimento (1-12): ")
    if mes_nacimiento_string.isnumeric():
        mes_nacimiento_numero = int(mes_nacimiento_string)
        if mes_nacimiento_numero >= 1 and mes_nacimiento_numero <=12:
            dia_nacimiento_string = input("Ingresa el dia de nacimiento: ")
            if dia_nacimiento_string.isnumeric():
                dia_nacimiento_numero = int(dia_nacimiento_string)
                if dia_nacimiento_numero >= 1 and  dia_nacimiento_numero <= 31:
                    anho_actual_string = input("Ingresa el año actual: ")
                    if anho_actual_string.isnumeric():
                        anho_actual_numero = int(anho_actual_string)
                        mes_actual_string = input("Ingresa el mes actual(1-12): ")
                        if mes_actual_string.isnumeric():                            
                            mes_actual_numero = int(mes_actual_string)
                            if mes_actual_numero >= 1 and mes_actual_numero <= 12:
                                dia_actual_string = input("Ingresa el dia actual: ")
                                if dia_actual_string.isnumeric():
                                    dia_actual_numeros = int(dia_actual_string)
                                    if dia_actual_numeros >=1 and dia_actual_numeros <= 31:
                                        # REGLA PARA SABER SI TODAVIA NO LLEGO NUESTRO CUMPLEAnhos
                                        # el mes de nacimiento es mayor que el mes actual 
                                        # OR
                                        # (el mes de naciemto es IGUAL a el mes actual) Y (el dia de nacimiento es mayor que el dia actual)                         
                                        if (mes_nacimiento_numero > mes_actual_numero) or ((mes_nacimiento_numero == mes_actual_numero) and (dia_nacimiento_numero > dia_actual_numeros)):
                                            #CASO TODAVIA NO LLEGO MI CUMPLEAÑOS
                                            edad = anho_actual_numero - anho_nacimiento_numero - 1
                                            if edad == -1:
                                                edad = 0
                                            mensaje = "Tu edad es " + str(edad) + " años"
                                            print(mensaje)
                                        else:
                                            #CASO YA LLEGO MI CUMPLEANHOS    
                                            edad = anho_actual_numero - anho_nacimiento_numero #esta formula es la correcta si es que ya llego mi cumpleaños
                                            mensaje = "Tu edad es " + str(edad) + " años"
                                            print(mensaje)
                                    else:
                                        print("ERRROR! el dia actual debe estar entre 1 y 31")
                                else:
                                    print("!ERROR el dia actual debe ser un numero")
                            else:
                                print("ERROR! el mes actual debe estar entre 1 y 12")
                        else:
                            print("ERROR! mes actual debe ser un numero")
                    else:
                        print("ERROR! el anho actual debe ser un numero")
                else:
                    print("ERROR! el dia de nacimeinto debe estar entre 1 y 31")
            else:
                print("ERROR! el dia de nacimiento debe ser un numero")
        else:
            print("ERROR! el mes de nacimiento debe estar entre 1 y 12")
    else:
        print("ERROR! en el mes de nacimiento debe ser un numero")
else:
    print("ERROR! El anho nacimiento debe ser un numero")