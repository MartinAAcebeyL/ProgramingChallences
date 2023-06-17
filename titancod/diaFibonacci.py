def fibonacci(numero: int = 30) -> str:
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)


N = 30
cadena = ""
for i in range(N + 1):
    cadena += str(fibonacci(i))

if __name__ == "__main__":
    m, d = list(map(str, input().split()))
    target = m + d
    if target in cadena:
        print("SI")
    else:
        print("NO")
