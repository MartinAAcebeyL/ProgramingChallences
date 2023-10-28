def suma_no_divisibles(A, B, C):
    total = ((B - A + 1) * (A + B)) // 2
    divisibles = C * (((B // C) * ((B // C) + 1) -
                      (A // C) * ((A // C) - 1)) // 2)
    return total - divisibles


T = int(input())  

for _ in range(T):
    A, B, C = map(int, input().split())
    A = min([A, B])
    B = max([A, B])
    resultado = suma_no_divisibles(A, B, C)
    print(resultado)
