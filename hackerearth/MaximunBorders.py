
cases = int(input())
for _ in range(cases):
    array = []
    N, M = list(map(int, input().split()))
    maximun = 0
    for _ in range(N):
        count_gato = input().count("#")
        if count_gato > maximun:
            maximun = count_gato
    print(maximun)
