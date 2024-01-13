# url: https://omegaup.com/arena/problem/Formula-Recursiva-Seis/

n = int(input())


def recursividad_6(number: int) -> int:
    if number <= 20:
        return 1
    return recursividad_6(number - 5) + 5 + number


result = recursividad_6(n)
print(result)
