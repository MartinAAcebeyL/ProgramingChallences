def maxima_operacion(a: int, b: int, c: int) -> int:
    return max(a+b+c, a*b*c, a*b+c, a+b*c, (a+b)*c, a*(b+c))


if __name__ == "__main__":
    numeros = list(map(int, input().split()))
    print(maxima_operacion(*numeros))
