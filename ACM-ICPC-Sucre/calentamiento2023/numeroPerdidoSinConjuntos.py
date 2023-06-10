def encontrar_carta_faltante(cartas):
    n = len(cartas) + 1
    suma_total = sum(range(1, n+1))
    suma_actual = sum(cartas)

    carta_faltante = suma_total - suma_actual
    return carta_faltante


if __name__ == "__main__":
    cantidad = int(input())
    cartas = list(map(int, input().split()))

    carta_faltante = encontrar_carta_faltante(cartas)
    print(carta_faltante)
