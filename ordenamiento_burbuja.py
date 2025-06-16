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