def pares(n: int, m: int):
    if n > m:
        raise Exception("No es posible continuar con la operación.")
    for i in range(n, m):
        if i % 2 == 0:
            print(i)


if __name__ == "__main__":
    n, m = list(map(int, input().split(" ")))
    pares(n, m)
