def encontrar_carta_faltante(cantidad: int, cartas: list) -> int:
    suma_total = sum(range(1, cantidad))
    suma_actual = sum(cartas)

    carta_faltante = suma_total - suma_actual
    return carta_faltante


if __name__ == "__main__":
    cantidad = int(input())
    cartas = list(map(int, input().split()))

    print(encontrar_carta_faltante(cantidad, cartas))
