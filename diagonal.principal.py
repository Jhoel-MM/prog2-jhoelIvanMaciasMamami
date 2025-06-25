def sumar_diagonal_principal(matriz):

    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma
def probar_sumar_diagonal_principal():
    print("\nProbando sumar_diagonal_principal...")