def cargar_combustible(vehiculo, litros_combustile):
        vehiculo["combustible_en_tanque"] += litros_combustile
        if vehiculo["combustible_en_tanque"] > vehiculo["capacidad_tanque"]:
            raise Exception("se supero la capacidad del tanque")
        
variableVehiculo = {
    "consumo_por_kilometro": 0.1,
    "capacidad_tanque": 40,
    "combustible_en_tanque": 0
}

cargar_combustible(variableVehiculo, 40)