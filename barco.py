import random

TAM = 5
NUM_BARCOS = 3
INTENTOS = 10
LETRAS = ['A', 'B', 'C', 'D', 'E']

def crear_tablero(valor='~'):
    return [[valor for _ in range(TAM)] for _ in range(TAM)]

def mostrar_tablero(tablero):
    print("   " + " ".join(str(i+1) for i in range(TAM)))
    for idx, fila in enumerate(tablero):
        print(f"{LETRAS[idx]}  " + " ".join(fila))
    print()

def colocar_barcos(tablero):
    barcos = 0
    while barcos < NUM_BARCOS:
        fila = random.randint(0, TAM - 1)
        col = random.randint(0, TAM - 1)
        if tablero[fila][col] != 'B':
            tablero[fila][col] = 'B'
            barcos += 1

def pedir_coordenadas(jugador):
    while True:
        entrada = input(f"{jugador}, ingresa coordenada (ej. A1 - E5): ").upper()
        if len(entrada) < 2 or len(entrada) > 3:
            print("❌ Formato inválido. Usa letra + número (Ej: B3).")
            continue
        fila_letra = entrada[0]
        col_str = entrada[1:]
        if fila_letra not in LETRAS or not col_str.isdigit():
            print("❌ Coordenada inválida.")
            continue
        fila = LETRAS.index(fila_letra)
        col = int(col_str) - 1
        if 0 <= fila < TAM and 0 <= col < TAM:
            return fila, col
        else:
            print("❌ Coordenadas fuera del tablero.")

def turno(jugador, tablero_visible, tablero_oculto):
    mostrar_tablero(tablero_visible)
    fila, col = pedir_coordenadas(jugador)

    if tablero_visible[fila][col] in ('X', 'O'):
        print("⚠️ Ya intentaste esa posición.")
        return 0

    if tablero_oculto[fila][col] == 'B':
        print("🔥 ¡Le diste a un barco!")
        tablero_visible[fila][col] = 'X'
        return 1
    else:
        print("🌊 Agua...")
        tablero_visible[fila][col] = 'O'
        return 0

def mostrar_barcos_restantes(tablero_oculto, tablero_visible):
    for i in range(TAM):
        for j in range(TAM):
            if tablero_oculto[i][j] == 'B' and tablero_visible[i][j] == '~':
                tablero_visible[i][j] = '🚢'

def jugar():
    print("🚢 ¡Bienvenido a Batalla Naval!")
    print("1. Jugar contra el bot")
    print("2. Jugar contra otro jugador")
    modo = input("Selecciona una opción (1 o 2): ")

    if modo == '2':
        nombre1 = input("👤 Nombre del Jugador 1: ")
        nombre2 = input("👤 Nombre del Jugador 2: ")
        jugadores = [nombre1, nombre2]
        tableros_ocultos = [crear_tablero(), crear_tablero()]
        tableros_visibles = [crear_tablero(), crear_tablero()]
        puntos = [0, 0]
        colocar_barcos(tableros_ocultos[0])
        colocar_barcos(tableros_ocultos[1])

        turno_actual = 0
        intentos_restantes = INTENTOS

        while intentos_restantes > 0 and (puntos[0] < NUM_BARCOS and puntos[1] < NUM_BARCOS):
            print(f"\nTurno de {jugadores[turno_actual]}")
            p = turno(
                jugadores[turno_actual],
                tableros_visibles[turno_actual],
                tableros_ocultos[1 - turno_actual]
            )
            puntos[turno_actual] += p
            intentos_restantes -= 1
            print(f"🟢 Puntos de {jugadores[0]}: {puntos[0]} | 🟣 Puntos de {jugadores[1]}: {puntos[1]}")
            turno_actual = 1 - turno_actual

        print("\n🎯 Juego terminado")
        if puntos[0] > puntos[1]:
            print(f"🏆 ¡{jugadores[0]} gana con {puntos[0]} puntos!")
        elif puntos[1] > puntos[0]:
            print(f"🏆 ¡{jugadores[1]} gana con {puntos[1]} puntos!")
        else:
            print("🤝 ¡Empate!")

        print("\n🔍 Mostrando todos los barcos restantes:")
        mostrar_barcos_restantes(tableros_ocultos[0], tableros_visibles[1])
        mostrar_tablero(tableros_visibles[1])
        mostrar_barcos_restantes(tableros_ocultos[1], tableros_visibles[0])
        mostrar_tablero(tableros_visibles[0])

    else:
        jugador = input("👤 Ingresa tu nombre: ")
        tablero_oculto = crear_tablero()
        tablero_visible = crear_tablero()
        colocar_barcos(tablero_oculto)
        aciertos = 0
        intentos_restantes = INTENTOS

        while intentos_restantes > 0 and aciertos < NUM_BARCOS:
            mostrar_tablero(tablero_visible)
            fila, col = pedir_coordenadas(jugador)

            if tablero_visible[fila][col] in ('X', 'O'):
                print("⚠️ Ya intentaste esa posición.")
                continue

            if tablero_oculto[fila][col] == 'B':
                print("🔥 ¡Le diste a un barco!")
                tablero_visible[fila][col] = 'X'
                aciertos += 1
            else:
                print("🌊 Agua...")
                tablero_visible[fila][col] = 'O'

            intentos_restantes -= 1
            print(f"Intentos restantes: {intentos_restantes} | Barcos hundidos: {aciertos}\n")

        mostrar_tablero(tablero_visible)
        if aciertos == NUM_BARCOS:
            print("🎉 ¡Felicidades! Hundiste todos los barcos.")
        else:
            print("💥 Te quedaste sin intentos. Perdiste.")
            print("🔍 Posiciones de los barcos enemigos:")
            mostrar_barcos_restantes(tablero_oculto, tablero_visible)
            mostrar_tablero(tablero_visible)

if __name__ == "__main__":
    jugar()
