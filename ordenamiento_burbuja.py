def ordenamiento_burbuja(lista):
  n = len(lista)
  for i in range(n-1):
    hubo_intercambio =False
    for j in range (n-1-i):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j + 1], lista[j]
            hubo_intercambio = True
    if not hubo_intercambio:
        break
  return lista
if __name__ == "__main__":
  numeros = [6, 3, 8, 2, 5]
  print("Antes:", numeros)
  ordenamiento_burbuja(numeros)
  print("Despues:", numeros)

lista_a_ordenar = [64, 34, 25, 12, 22, 11, 90]
print(f"\nLista original: {lista_a_ordenar}")
ordenamiento_burbuja(lista_a_ordenar)
print(f"Lista ordenada: {lista_a_ordenar}")
# Caso 1: Lista desordenada
lista1 = [6, 3, 8, 2, 5]
ordenamiento_burbuja(lista1)
assert lista1 == [2, 3, 5, 6, 8], "Fallo en Caso 1"
# Caso 2: Lista ya ordenada
lista2 = [1, 2, 3, 4, 5]
ordenamiento_burbuja(lista2)
assert lista2 == [1, 2, 3, 4, 5], "Fallo en Caso 2"
# Caso 3: Lista ordenada a la inversa
lista3 = [5, 4, 3, 2, 1]
ordenamiento_burbuja(lista3)
assert lista3 == [1, 2, 3, 4, 5], "Fallo en Caso 3"
# Caso 4: Lista con elementos duplicados
lista4 = [5, 1, 4, 2, 2, 8]
ordenamiento_burbuja(lista4)
assert lista4 == [1, 2, 2, 4, 5, 8], "Fallo en Caso 4"
# Casos borde
assert ordenamiento_burbuja([]) == []
assert ordenamiento_burbuja([42]) == [42], "Fallo en Casos borde"
print("\n¡Todas las pruebas pasaron!")