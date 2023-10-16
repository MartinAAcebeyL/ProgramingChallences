def calcular_potencia_modulo(a, b, m):
    if b == 0:
        return 1
    if b % 2 == 0:
        temp = calcular_potencia_modulo(a, b // 2, m)
        return (temp * temp) % m
    else:
        temp = calcular_potencia_modulo(a, (b - 1) // 2, m)
        return (a * temp * temp) % m

T = int(input())

for _ in range(T):
    a, b, m = map(int, input().split())
    resultado = calcular_potencia_modulo(a, b, m)
    print(resultado)
