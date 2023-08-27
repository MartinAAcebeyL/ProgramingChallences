def localizar_1(matriz: list[list[int]]) -> list[int]:
    coordenadas = []
    for index, fila in enumerate(matriz):
        if 1 in fila:
            coordenadas.append(index)
            coordenadas.append(fila.index(1))
            break
    return coordenadas


def cuanto_falta_centro(coodenadas: list[int]) -> int:
    return abs(coodenadas[0]-2)+abs(coodenadas[1]-2)


matriz = []
for _ in range(5):
    fila = list(map(int, input().split()))
    matriz.append(fila)

coordenadas = localizar_1(matriz=matriz)
print(coordenadas)
