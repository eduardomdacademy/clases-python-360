class Cedula:
    def __init__(self, nombre, numero, nacionalidad, fecha_expedicion, fecha_vencimiento):
        self.nombre = nombre
        self.numero = numero
        self.nacionalidad = nacionalidad
        self.fecha_expedicion = fecha_expedicion
        self.fecha_vencimiento = fecha_vencimiento
    
    def imprimir_datos(self):
        print("nombre:", self.nombre)
        print("numero:", self.numero)


variableCedula = Cedula("Eduardo", 5555555, "paraguaya", "2025-01-01","2026-01-01")
varuableCedula2 = Cedula("Luis Lopez", 664466, "paraguaya", "2025-01-01","2026-01-01")

variableCedula.imprimir_datos()
varuableCedula2.imprimir_datos()