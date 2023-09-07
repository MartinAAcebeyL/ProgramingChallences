N = int(input())
ARRAY = [int(i) for i in input().split()]


def sumatoria(indice: int) -> int:
    iteraciones = (N-indice)//3
    if iteraciones != 0:
        return sum(ARRAY[indice:indice+(3*iteraciones)])
    return sum(ARRAY[indice:indice+1])


may = 0
for i in range(N):
    suma = sumatoria(i)
    if suma > may:
        may = suma
print(may)
