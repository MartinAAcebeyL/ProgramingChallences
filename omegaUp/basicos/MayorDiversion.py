# link: https://omegaup.com/arena/problem/edm2021n1-diversion/
def encontrar_mayor_diversion(juguetes: list) -> int:
    menor = min(juguetes)
    return sum(j for j in juguetes if j != menor)


if __name__ == "__main__":
    cantidad_juguetes = int(input())
    lista_juguetes = [int(input()) for _ in range(cantidad_juguetes)]
