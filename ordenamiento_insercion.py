def ordenamiento_insercion(lista):
  for i in range(1, len(lista)):
      valor_actual = lista[i]
      posicion_actual = i

      while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
          lista[posicion_actual] = lista[posicion_actual - 1]
          posicion_actual -= 1

      lista[posicion_actual] = valor_actual

  return lista
lista = [18, 3, 9, 5, 2, 0, 34, 6]
lista_ordenada = ordenamiento_insercion(lista)
print(lista_ordenada)
print("\n--- lista ordenada con exito ---")
print("Jhoel Ivan Macias Mamani")