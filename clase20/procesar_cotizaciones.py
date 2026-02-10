import pandas as pd
import openpyxl
from pathlib import Path
from datetime import datetime

def extraer_monedas(df_raw, fila_monedas, fila_tipo):
    """
    Extrae las monedas y sus columnas de compra/venta de una tabla.

    Args:
        df_raw: DataFrame sin procesar
        fila_monedas: Índice de la fila que contiene los nombres de monedas
        fila_tipo: Índice de la fila que contiene "Compra"/"Venta"

    Returns:
        Diccionario con {nombre_moneda: {'compra': col_idx, 'venta': col_idx}}
    """
    monedas = {}
    for col_idx in range(1, len(df_raw.columns)):
        moneda = df_raw.iloc[fila_monedas, col_idx]
        tipo = df_raw.iloc[fila_tipo, col_idx]

        if pd.notna(moneda) and moneda != '' and moneda != '-':
            # Nueva moneda encontrada
            moneda_nombre = str(moneda).strip()
            # Filtrar monedas inválidas
            if moneda_nombre not in monedas and moneda_nombre != '-':
                monedas[moneda_nombre] = {'compra': None, 'venta': None}

            # Determinar si es columna de compra o venta
            if pd.notna(tipo):
                tipo_str = str(tipo).strip().lower()
                if 'compra' in tipo_str:
                    monedas[moneda_nombre]['compra'] = col_idx
                elif 'venta' in tipo_str:
                    monedas[moneda_nombre]['venta'] = col_idx
        elif pd.notna(tipo):
            # Es una columna de compra/venta de la moneda anterior
            tipo_str = str(tipo).strip().lower()
            if monedas and 'venta' in tipo_str:
                # Asignar a la última moneda
                ultima_moneda = list(monedas.keys())[-1]
                monedas[ultima_moneda]['venta'] = col_idx

    return monedas

def procesar_datos_moneda(df_raw, fila_datos_inicio, cols):
    """
    Procesa los datos de cotización de una moneda.

    Args:
        df_raw: DataFrame sin procesar
        fila_datos_inicio: Índice de la primera fila con datos
        cols: Diccionario con {'compra': col_idx, 'venta': col_idx}

    Returns:
        Lista de diccionarios con {Día, Compra, Venta}
    """
    datos_moneda = []

    for fila_idx in range(fila_datos_inicio, len(df_raw)):
        dia = df_raw.iloc[fila_idx, 0]

        # Si no hay día, terminar
        if pd.isna(dia):
            break

        # Verificar si el día es un número válido
        try:
            dia_num = int(dia)
        except (ValueError, TypeError):
            # No es un número válido (puede ser "Promedio", etc.), continuar
            continue

        compra = df_raw.iloc[fila_idx, cols['compra']] if cols['compra'] is not None else None
        venta = df_raw.iloc[fila_idx, cols['venta']] if cols['venta'] is not None else None

        # Solo agregar si hay al menos un valor válido
        if not (pd.isna(compra) and pd.isna(venta)):
            # Convertir '-' a NaN
            if compra == '-':
                compra = None
            if venta == '-':
                venta = None

            datos_moneda.append({
                'Día': dia_num,
                'Compra': compra,
                'Venta': venta
            })

    return datos_moneda

def procesar_tabla(df_raw, fila_monedas, fila_tipo, fila_datos_inicio):
    """
    Procesa una tabla completa de cotizaciones.

    Args:
        df_raw: DataFrame sin procesar
        fila_monedas: Índice de la fila con nombres de monedas
        fila_tipo: Índice de la fila con "Compra"/"Venta"
        fila_datos_inicio: Índice de la primera fila con datos

    Returns:
        Diccionario con {nombre_moneda: [datos]}
    """
    # Extraer monedas y sus columnas
    monedas = extraer_monedas(df_raw, fila_monedas, fila_tipo)

    # Procesar datos de cada moneda
    resultado = {}
    for moneda, cols in monedas.items():
        datos = procesar_datos_moneda(df_raw, fila_datos_inicio, cols)
        if datos:  # Solo agregar si hay datos
            resultado[moneda] = datos

    return resultado

def procesar_cotizaciones():
    """
    Lee el archivo Excel con cotizaciones diarias y genera un nuevo Excel
    con una hoja por cada moneda, mostrando la cotización de compra/venta por día.
    """

    # Ruta del archivo de entrada
    carpeta_cotizacion = Path("cotizacion")
    archivo_entrada = carpeta_cotizacion / "Cotizaciones - Agosto 2025.xlsx"

    # Verificar que el archivo existe
    if not archivo_entrada.exists():
        print(f"Error: No se encontró el archivo {archivo_entrada}")
        return

    print(f"Leyendo archivo: {archivo_entrada}")

    # Leer el archivo Excel sin procesar
    try:
        df_raw = pd.read_excel(archivo_entrada, sheet_name="Cotizaciones Diarias", header=None)
        print(f"\nDatos leídos correctamente. Shape: {df_raw.shape}")

        # Buscar el mes/año en las primeras filas (típicamente fila 7, columna 1)
        mes_anio = None
        for idx in range(min(10, len(df_raw))):
            for col in df_raw.columns:
                val = df_raw.iloc[idx, col]
                if pd.notna(val) and isinstance(val, str) and "/" in val:
                    mes_anio = val
                    print(f"Mes/Año encontrado: {mes_anio}")
                    break
            if mes_anio:
                break

        # Configuración de las tres tablas
        tablas = [
            {'fila_monedas': 9, 'fila_tipo': 10, 'fila_datos_inicio': 11, 'nombre': 'Primera tabla'},
            {'fila_monedas': 59, 'fila_tipo': 60, 'fila_datos_inicio': 61, 'nombre': 'Segunda tabla'},
            {'fila_monedas': 108, 'fila_tipo': 109, 'fila_datos_inicio': 110, 'nombre': 'Tercera tabla'}
        ]

        # Procesar ambas tablas y consolidar todas las monedas
        todas_monedas = {}
        for config in tablas:
            print(f"\nProcesando {config['nombre']}...")
            monedas_tabla = procesar_tabla(
                df_raw,
                config['fila_monedas'],
                config['fila_tipo'],
                config['fila_datos_inicio']
            )

            # Agregar monedas al diccionario consolidado
            for moneda, datos in monedas_tabla.items():
                if moneda in todas_monedas:
                    # Si la moneda ya existe, agregar sufijo
                    print(f"  Advertencia: Moneda '{moneda}' duplicada, agregando sufijo")
                    moneda = f"{moneda}_2"

                todas_monedas[moneda] = datos

        print(f"\nTotal de monedas encontradas: {len(todas_monedas)}")
        print(f"Monedas: {list(todas_monedas.keys())}")

        # Crear archivo Excel de salida
        archivo_salida = carpeta_cotizacion / f"Cotizaciones_Por_Moneda_{mes_anio.replace('/', '_')}.xlsx"

        print(f"\nGenerando archivo Excel de salida...")
        with pd.ExcelWriter(archivo_salida, engine='openpyxl') as writer:
            for moneda, datos_moneda in todas_monedas.items():
                # Crear DataFrame para esta moneda
                df_moneda = pd.DataFrame(datos_moneda)

                # Guardar en una hoja con el nombre de la moneda
                nombre_hoja = moneda[:31]  # Excel limita nombres de hoja a 31 caracteres
                df_moneda.to_excel(writer, sheet_name=nombre_hoja, index=False)

                print(f"  - {moneda}: {len(df_moneda)} registros guardados")

        print(f"\nArchivo generado exitosamente: {archivo_salida}")

    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        import traceback
        traceback.print_exc()
        return

if __name__ == "__main__":
    procesar_cotizaciones()
