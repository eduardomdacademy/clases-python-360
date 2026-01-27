cedula = {
    "nombre": "Eduardo",
    "numero": "555.555",
    "nacionalidad": "paraguaya",
    "fecha_expedicion":"2025-01-01",
    "fecha_vencimiento":"2026-01-01"
}

def validar_cedula(cedula):
    if cedula["fecha_vencimiento"] <= "2025-01-26":
        return False
    if len(cedula["nombre"]) == 0:
        return False
    if len(cedula["numero"]) == 0:
        return
    return True