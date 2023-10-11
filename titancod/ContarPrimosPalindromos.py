import sys


def generar_criba(n: int = 10000000):
    criba = [True] * (n + 1)
    criba[0] = criba[1] = False

    for i in range(2, int(n**0.5) + 1):
        if criba[i]:
            for j in range(i * i, n + 1, i):
                criba[j] = False
    return criba


def reverse(number):
    reversed_num = 0
    while number != 0:
        reversed_num = reversed_num * 10 + number % 10
        number = number // 10
    return reversed_num


CRIBA = generar_criba()


for data in sys.stdin:
    a, b = list(map(int, data.split()))

    count = 0
    for i in range(a, b+1):
        if CRIBA[i] and CRIBA[reverse(i)]:
            count += 1
    print(count)
