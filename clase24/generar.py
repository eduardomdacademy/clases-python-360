import xlwt
from datetime import date
import random

wb = xlwt.Workbook()
ws = wb.add_sheet("Transacciones")

# --- Estilos ---
header_style = xlwt.easyxf(
    "font: bold on, colour white, height 240;"
    "pattern: pattern solid, fore_colour dark_blue;"
    "alignment: horiz centre, vert centre;"
    "borders: left thin, right thin, top thin, bottom thin;"
)
date_style = xlwt.easyxf(
    "alignment: horiz centre;"
    "borders: left thin, right thin, top thin, bottom thin;",
    num_format_str="YYYY-MM-DD",
)
date_style_alt = xlwt.easyxf(
    "alignment: horiz centre;"
    "pattern: pattern solid, fore_colour light_blue;"
    "borders: left thin, right thin, top thin, bottom thin;",
    num_format_str="YYYY-MM-DD",
)
text_style = xlwt.easyxf(
    "borders: left thin, right thin, top thin, bottom thin;"
)
text_style_alt = xlwt.easyxf(
    "pattern: pattern solid, fore_colour light_blue;"
    "borders: left thin, right thin, top thin, bottom thin;"
)
money_style = xlwt.easyxf(
    "alignment: horiz right;"
    "borders: left thin, right thin, top thin, bottom thin;",
    num_format_str="#,##0.00",
)
money_style_alt = xlwt.easyxf(
    "alignment: horiz right;"
    "pattern: pattern solid, fore_colour light_blue;"
    "borders: left thin, right thin, top thin, bottom thin;",
    num_format_str="#,##0.00",
)
center_style = xlwt.easyxf(
    "alignment: horiz centre;"
    "borders: left thin, right thin, top thin, bottom thin;"
)
center_style_alt = xlwt.easyxf(
    "alignment: horiz centre;"
    "pattern: pattern solid, fore_colour light_blue;"
    "borders: left thin, right thin, top thin, bottom thin;"
)
# Estilos para ingresos (verde)
date_style_green = xlwt.easyxf(
    "alignment: horiz centre;"
    "pattern: pattern solid, fore_colour light_green;"
    "borders: left thin, right thin, top thin, bottom thin;",
    num_format_str="YYYY-MM-DD",
)
text_style_green = xlwt.easyxf(
    "pattern: pattern solid, fore_colour light_green;"
    "borders: left thin, right thin, top thin, bottom thin;"
)
money_style_green = xlwt.easyxf(
    "alignment: horiz right;"
    "pattern: pattern solid, fore_colour light_green;"
    "borders: left thin, right thin, top thin, bottom thin;",
    num_format_str="#,##0.00",
)
center_style_green = xlwt.easyxf(
    "alignment: horiz centre;"
    "pattern: pattern solid, fore_colour light_green;"
    "borders: left thin, right thin, top thin, bottom thin;"
)

# --- Encabezados ---
headers = ["Fecha", "Descripción", "Monto", "Tipo"]
col_widths = [4500, 10000, 4500, 3500]

for col, (h, w) in enumerate(zip(headers, col_widths)):
    ws.write(0, col, h, header_style)
    ws.col(col).width = w

# --- Datos de transacciones ---
random.seed(42)  # Reproducible

gastos = [
    ("Starbucks", 4.50, 7.50, 6),
    ("Supermercado La Colonia", 45.00, 120.00, 4),
    ("McDonald's", 6.00, 12.00, 3),
    ("Netflix", 15.99, 15.99, 1),
    ("Spotify", 9.99, 9.99, 1),
    ("Uber", 5.00, 18.00, 5),
    ("Gasolinera Puma", 30.00, 55.00, 3),
    ("Farmacia del Pueblo", 8.00, 45.00, 2),
    ("Restaurante El Fogón", 15.00, 35.00, 2),
    ("Pago de Luz (ANDE)", 35.00, 60.00, 1),
    ("Pago de Agua (ESSAP)", 15.00, 25.00, 1),
    ("Internet Tigo", 29.99, 29.99, 1),
    ("Alquiler Apartamento", 450.00, 450.00, 1),
    ("Gimnasio SportLife", 25.00, 25.00, 1),
    ("Librería El Lector", 10.00, 30.00, 1),
    ("Steam - Videojuegos", 10.00, 45.00, 1),
    ("Tienda de Ropa Zara", 35.00, 80.00, 1),
    ("Panadería Don Vito", 3.00, 8.00, 4),
    ("Estacionamiento Centro", 2.00, 5.00, 3),
    ("Cine Multicenter", 8.00, 12.00, 1),
]

transactions = []
for month in range(1, 4):
    transactions.append((date(2026, month, 1), "Salario Mensual", 1500.000, "Ingreso"))

    if random.random() > 0.3:
        d = random.randint(10, 28)
        amt = round(random.uniform(200, 500), 2)
        transactions.append((date(2026, month, d), "Freelance Diseño Web", amt, "Ingreso"))

    for desc, lo, hi, freq in gastos:
        n = freq if random.random() > 0.2 else freq + random.choice([-1, 0, 1])
        n = max(0, n)
        days_used = sorted(random.sample(range(1, 29), min(n, 28)))
        for d in days_used:
            amt = round(random.uniform(lo, hi), 2) if lo != hi else lo
            transactions.append((date(2026, month, d), desc, amt, "Gasto"))

# Gasto grande para flaggear
transactions.append((date(2026, 2, 14), "Tienda Electrónica - TV Samsung", 650.000, "Gasto"))

# Duplicado intencional
transactions.append((date(2026, 1, 15), "Gasolinera Puma", 42.500, "Gasto"))
transactions.append((date(2026, 1, 15), "Gasolinera Puma", 42.500, "Gasto"))

transactions.sort(key=lambda x: x[0])

# --- Escribir datos ---
for i, (fecha, desc, monto, tipo) in enumerate(transactions):
    row = i + 1
    is_alt = row % 2 == 0
    is_income = tipo == "Ingreso"

    if is_income:
        ds, ts, ms, cs = date_style_green, text_style_green, money_style_green, center_style_green
    elif is_alt:
        ds, ts, ms, cs = date_style_alt, text_style_alt, money_style_alt, center_style_alt
    else:
        ds, ts, ms, cs = date_style, text_style, money_style, center_style

    ws.write(row, 0, fecha, ds)
    ws.write(row, 1, desc, ts)
    ws.write(row, 2, monto * 6000, ms)
    ws.write(row, 3, tipo, cs)

wb.save("transacciones.xls")
print(f"✅ Archivo generado: transacciones.xls")
print(f"   Total de transacciones: {len(transactions)}")
print(f"   Período: Enero - Marzo 2026")
