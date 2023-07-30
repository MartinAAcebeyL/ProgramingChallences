

coordenadas = []

for _ in range(4):
    coordenadas.append(list(map(int, input().split())))

xs = []
ys = []

punto1 = coordenadas.pop(0)

for coordenada in coordenadas:
    index = coordenadas.index(coordenada)
    if coordenada[0] == punto1[0]:
        xs.append(coordenadas.pop(index))
        xs.append(punto1)
        ys = coordenadas
        break
    elif coordenada[1] == punto1[1]:
        ys.append(coordenadas.pop(index))
        ys.append(punto1)
        xs = coordenadas
        break


print(xs[0][0], ys[0][1])
