class Cotizacion:
    def __init__(self, fecha: str, moneda:str, compra:int, venta:int):
        self.fecha = fecha
        self.moneda = moneda
        self.compra = compra
        self.venta = venta

    def imprimir(self):
        print(self.fecha,"|", self.moneda, "|", self.compra, "|", self.venta)
    
    def __lt__(self, other):
        self_fecha = self.fecha.split("-")
        other_fecha = other.fecha.split("-")
        self_anho = int(self_fecha[0])
        other_anho = int(other_fecha[0])
        self_mes = int(self_fecha[1])
        other_mes = int(other_fecha[1])
        self_dia = int(self_fecha[2])
        other_dia = int(other_fecha[2])

        if self_anho != other_anho:
            return self_anho < other_anho
        if self_mes != other_mes:
            return self_mes < other_mes
        return self_dia < other_dia