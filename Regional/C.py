def es_posible_elegir(n, k, x):
    suma_prim_k = (k * (k + 1)) // 2
    if suma_prim_k > x:
        return "NO"

    suma_ult_k = (n * (n + 1)) // 2 - ((n - k) * (n - k + 1)) // 2
    if suma_ult_k < x:
        return "NO"

    return "YES"


t = int(input())

for _ in range(t):
    n, k, x = map(int, input().split())
    respuesta = es_posible_elegir(n, k, x)
    print(respuesta)
