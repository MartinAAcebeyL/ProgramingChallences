# url: https://www.titancod.net/problema/ESCALERAS

def acomodar_cajas(altura: int, caso: list) -> int:
    cajas = 0
    for i in range(1, altura+1):
        if caso[i-1] > i:
            diferencia = caso[i-1]-i
            cajas += diferencia
    print(cajas)


if __name__ == "__main__":
    c = int(input())
    array_casos = []

    for _ in range(c):
        casos = list(map(int, input().split()))
        array_casos.append(casos)

    for i in array_casos:
        acomodar_cajas(i[0], i[1:])
