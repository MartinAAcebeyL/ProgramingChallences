N = 664579


def generar_criba(n: int):
    criba = [True] * (n + 1)
    criba[0] = criba[1] = False

    for i in range(2, int(n**0.5) + 1):
        if criba[i]:
            for j in range(i * i, n + 1, i):
                criba[j] = False
    r = []
    for index, i in enumerate(criba):
        if i:
            r.append(index)

    return r


def imprimir(inicio: int, final: int):
    numbers = CRIBA[inicio:final]
    return ' '.join(map(str, numbers[::-1]))+' '+' '.join(map(str, numbers[1:]))


casos = int(input())
CRIBA = generar_criba(N)


for _ in range(casos):
    inicio, final = list(map(int, input().split()))
    print(imprimir(inicio, final+1))
