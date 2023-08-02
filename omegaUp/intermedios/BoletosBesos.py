
# url: https://omegaup.com/arena/problem/bpb/
def sumar_digitos(number: int) -> int:
    suma = 0
    while number > 0:
        digito = number % 10
        suma += digito
        number //= 10
    return suma


if __name__ == "__main__":
    n = int(input())
    cont = 0
    while True:
        if n > 9999999:
            n = 0
        if sumar_digitos(n) == 21:
            ceros = 7-len(str(n))
            print(cont, "0"*ceros+f"{n}")
            break

        cont += 1
        n += 1

