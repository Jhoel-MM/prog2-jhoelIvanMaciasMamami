import random

# Tamaño del tablero
TAM = 5
NUM_BARCOS = 5
INTENTOS = 10

# Crear el tablero vacío
def crear_tablero(valor='~'):
    return [[valor for _ in range(TAM)] for _ in range(TAM)]

# Mostrar el tablero al usuario
def mostrar_tablero(tablero):
    print("  " + " ".join(str(i) for i in range(TAM)))
    for idx, fila in enumerate(tablero):
        print(f"{idx} " + " ".join(fila))
    print()

# Posicionar barcos aleatoriamente
def colocar_barcos(tablero):
    barcos = 0
    while barcos < NUM_BARCOS:
        fila = random.randint(0, TAM - 1)
        col = random.randint(0, TAM - 1)
        if tablero[fila][col] != 'B':
            tablero[fila][col] = 'B'
            barcos += 1

# Lógica del juego
def jugar():
    tablero_oculto = crear_tablero()
    tablero_jugador = crear_tablero()
    colocar_barcos(tablero_oculto)

    print("🚢 ¡Bienvenido a Batalla Naval!")
    print(f"Hay {NUM_BARCOS} barcos ocultos en un tablero de {TAM}x{TAM}.")
    print(f"Tienes {INTENTOS} intentos para hundirlos todos -- BUENA SUERTE.--\n")

    aciertos = 0
    intentos_restantes = INTENTOS

    while intentos_restantes > 0 and aciertos < NUM_BARCOS:
        mostrar_tablero(tablero_jugador)
        try:
            fila = int(input("Ingresa la fila (0-4): "))
            col = int(input("Ingresa la columna (0-4): "))
        except ValueError:
            print("❌ Entrada inválida. Usa números.")
            continue

        if fila < 0 or fila >= TAM or col < 0 or col >= TAM:
            print("❌ Coordenadas fuera del tablero.")
            continue

        if tablero_jugador[fila][col] in ('X', 'O'):
            print("⚠️ Ya intentaste esa posición.")
            continue

        if tablero_oculto[fila][col] == 'B':
            print("🔥 ¡Le diste a un barco!")
            tablero_jugador[fila][col] = 'X'
            aciertos += 1
        else:
            print("🌊 Agua...")
            tablero_jugador[fila][col] = 'O'

        intentos_restantes -= 1
        print(f"Intentos restantes: {intentos_restantes}\n")

    mostrar_tablero(tablero_jugador)
    if aciertos == NUM_BARCOS:
        print("🎉 ¡Felicidades! Hundiste todos los barcos.")
    else:
        print("💥 Te quedaste sin intentos. Perdiste.")
        print("Posiciones de los barcos enemigas:")
        for i in range(TAM):
            for j in range(TAM):
                if tablero_oculto[i][j] == 'B':
                    tablero_jugador[i][j] = 'B'
        mostrar_tablero(tablero_jugador)

# Ejecutar el juego
if __name__ == "__main__":
    jugar()
