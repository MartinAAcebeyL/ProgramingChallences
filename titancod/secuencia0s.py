import sys


def convert_to_bin(number: int) -> list:
    l = []
    for i in range(2**number):
        binario = bin(i)[2:].zfill(number)
        l.append(binario)
    return l


def contador_secuencia(conmbinaciones: list, number: int) -> int:
    cont = 0
    for combinacion in conmbinaciones:
        for i in range(number-1):
            if combinacion[i] == '0' and combinacion[i] == combinacion[i+1]:
                cont += 1
                break
    return 2**number-cont


while True:
    number = int(input())
    if number == 0:
        break

    r = contador_secuencia(convert_to_bin(number), number)
    print(r)
