# url:https://www.titancod.net/problema/PARIMP
def create_109_primos(n: int = 109) -> list:
    fib_list = [0, 1]
    while len(fib_list) < n:
        next_number = fib_list[-1] + fib_list[-2]
        fib_list.append(next_number)
    return fib_list


PRIMOS = create_109_primos()


if __name__ == "__main__":
    print(PRIMOS)
    c = int(input())
    for i in range(c):
        n = int(input())
        if PRIMOS[n] % 2 == 0:
            print(f"{PRIMOS[n]} par")
        else:
            print(f"{PRIMOS[n]} impar")
