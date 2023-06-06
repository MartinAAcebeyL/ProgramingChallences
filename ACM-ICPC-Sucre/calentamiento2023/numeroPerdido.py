if __name__ == "__main__":
    cantidad = int(input())
    numeros = map(int, input().split())

    conjunto_dado = set(numeros)
    universo = set(range(1, cantidad+1))
    numero_perdido = universo - conjunto_dado
    print(numero_perdido.pop())