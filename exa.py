def calcular_promedio(lista):
    total = 0
    for num in lista:
        total += num
    return total / len(lista)

print(calcular_promedio([5, 10, 15]))