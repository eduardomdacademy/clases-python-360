from openai import OpenAI
from tablero import Tablero
def pedi_jugada_chatgpt(tablero:Tablero):
    client = OpenAI(
        api_key="COLOCA ACA TU APIKEY",
    )   
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions="Sos un AI que juega TaTeTI, tu respuesta debe ser exclusivamente en formato texto sin explicacion ni nada adicional <valor_fila>,<valor_columna> tu marca es \"O\" y el estado actual del tablero es las filas van de 0 a 2 y las columnas van de 0 a 2",
        input= tablero.generar_texto_tablero()
    )
    respuesta = response.output_text.split(",")
    fila = int(respuesta[0])
    col = int(respuesta[1])
    return fila, col