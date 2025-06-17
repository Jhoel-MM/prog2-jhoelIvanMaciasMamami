def merge_sort(lista):
  if len(lista) <= 1:
      return lista

  medio = len(lista) // 2
  mitad_izquierda = lista[:medio]
  mitad_derecha = lista[medio:]

  izquierda_ordenada = merge_sort(mitad_izquierda)
  derecha_ordenada = merge_sort(mitad_derecha)

  print(f"Mezclaria {izquierda_ordenada} y {derecha_ordenada}")

  return merge(izquierda_ordenada, derecha_ordenada)

def merge(izquierda, derecha):
  resultado = []
  i = 0
  j = 0

  while i < len(izquierda) and j < len(derecha):
      if izquierda[i] < derecha[j]:
          resultado.append(izquierda[i])
          i += 1
      else:
          resultado.append(derecha[j])
          j += 1

  resultado.extend(izquierda[i:])
  resultado.extend(derecha[j:])

  return resultado

lista = [5, 2, 9, 1, 5, 6]
resultado = merge_sort(lista)
print("Lista ordenada:", resultado)