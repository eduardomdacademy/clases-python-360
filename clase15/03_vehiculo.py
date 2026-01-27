class Vehiculo:
    def __init__(self, consumo_por_kilometro, capacidad_tanque):
        self.consumo_por_kilometro = consumo_por_kilometro
        self.capacidad_tanque = capacidad_tanque
        self.combustible_en_tanque = 0
    
    def cargar_combustible(self, litros_combustile):
        self.combustible_en_tanque += litros_combustile
        if self.combustible_en_tanque > self.capacidad_tanque:
            raise Exception("se supero la capacidad del tanque")
    
    def recorrer(self, kilometros):
        self.combustible_en_tanque -= (self.consumo_por_kilometro * kilometros)
        if self.combustible_en_tanque < 0:
            raise Exception("se consumio mas combustible del que habia en el tanque")
        
    def calcular_que_tan_lejos_podemos_llegar(self):
        return self.combustible_en_tanque / self.consumo_por_kilometro

variableVehiculo = Vehiculo(0.1,40)
variableVehiculo.cargar_combustible(30)
variableVehiculo.recorrer(120)

print("quedan ",variableVehiculo.combustible_en_tanque, "litos de combustible")
try:
    print("queda combustible suficiente para recorer ",variableVehiculo.calcular_que_tan_lejos_podemos_llegar(), "kilometros")    
    variableVehiculo.recorrer(400)
except:
    print("El vehiculo paro en mitad del camino porque se quedo sin combustible")