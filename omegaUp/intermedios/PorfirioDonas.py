def puedeComprarDonas(N, A, B, preguntas):
    for i in range(N):
        X = preguntas[i]
        if X % A == 0 or X % B == 0 or X % (A + B) == 0:
            print("Si")
        else:
            print("No")

N, A, B = map(int, input().split())
preguntas = []
for _ in range(N):
    X = int(input())
    preguntas.append(X)

puedeComprarDonas(N, A, B, preguntas)