# Definimos la función que suma todos los elementos de una matriz
def sumar_total_matriz(matriz):
    """
    Esta función recibe una matriz (lista de listas)
    y retorna la suma total de todos sus elementos.
    Ejemplo:
    matriz = [[1, 2], [3, 4]]
    resultado = 10
    """
    total = 0
    for fila in matriz:
        for elemento in fila:
            total += elemento
    return total

# Función para probar que sumar_total_matriz funciona correctamente
def probar_suma_total():
    print("Probando sumar_total_matriz...")

    # Caso 1: matriz normal
    m1 = [[1, 2, 3], [4, 5, 6]]
    assert sumar_total_matriz(m1) == 21  # 1+2+3+4+5+6 = 21

    # Caso 2: matriz con negativos y ceros
    m2 = [[-1, 0, 1], [10, -5, 5]]
    assert sumar_total_matriz(m2) == 10  # -1+0+1+10-5+5 = 10

    # Casos borde o límites
    assert sumar_total_matriz([[]]) == 0         # Matriz con una fila vacía
    assert sumar_total_matriz([]) == 0           # Matriz completamente vacía
    assert sumar_total_matriz([[42]]) == 42      # Matriz de un solo elemento

    print("\n ¡Pruebas para sumar_total_matriz pasaron!")
    print("Jhoel Ivan Macias Mamani")

# Llamamos a la función de pruebas
probar_suma_total()