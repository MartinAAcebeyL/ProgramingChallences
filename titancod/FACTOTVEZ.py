# url: https://www.titancod.net/problema/FACTOTVEZ

def factorial(n: int):
    number = 1
    for i in range(2, n+1):
        number *= i
    return number


def ACMnumber_decimal(n: str, size: int) -> int:
    result = 0
    for i in range(size):
        result += int(n[i])*factorial(size-i)
    return result


if __name__ == "__main__":
    numbers = []
    while True:
        n = input()

        if n == "0":
            break
        numbers.append(n)

    for number in numbers:
        print(ACMnumber_decimal(number, len(number)))
