class Email:
    def __init__(self, email):
        self.email = email.strip()
    def obtener_dominio(self):
        lista = self.email.split("@")
        if len(lista) != 2:
            raise Exception("un mail debe tener dos partes separadas por @")
        dominio = lista[1]
        if len(dominio) == 0:
            raise Exception("El dominio no puede ser vacio")
        if len(lista[0]) == 0:
            raise Exception("La primera parte del mail no puede ser vacia")
        return dominio