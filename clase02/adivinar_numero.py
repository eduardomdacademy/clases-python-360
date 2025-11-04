import random

def saludar_jugador():
    print("¡Bienvenido a 'Adivina el Número'!")
    print("Estoy pensando en un número entre 1 y 100.")
    print("¿Puedes adivinar cuál es?")

def obtener_intento():
    while True:
        try:
            intento = int(input("Ingresa tu intento: "))
            return intento
        except ValueError:
            print("Por favor, ingresa un número válido.")

def jugar():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    while not adivinado:
        intento = obtener_intento()
        intentos += 1

        if intento < numero_secreto:
            print("¡Demasiado bajo! Intenta de nuevo.")
        elif intento > numero_secreto:
            print("¡Demasiado alto! Intenta de nuevo.")
        else:
            print(f" ¡Correcto! Lo adivinaste en {intentos} intentos.")
            adivinado = True            
            input("presiona cualquier tecla para continuar...")

if __name__ == "__main__":
    saludar_jugador()
    jugar()