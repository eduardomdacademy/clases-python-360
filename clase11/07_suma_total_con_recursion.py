lista = [12,4,5,7,12,1]
def sumar_lista(lista, indice):
    print("empieza invocacion con indice", indice)
    if indice == len(lista)- 1:
        print("llegamos al final y retornamos el valor del ultimo elemento",lista[indice])
        return lista[indice]
    else:
        nuevo_indice = indice + 1
        resultado = lista[indice] + sumar_lista(lista, nuevo_indice)
        print("invocacion con indice", indice, "retorna resultado", resultado)
        return resultado
    
resultado = sumar_lista(lista, 0)
print(resultado)