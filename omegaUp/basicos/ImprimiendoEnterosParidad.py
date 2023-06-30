def _main() -> None:
    N = int(input())
    arreglo = map(int, input().split(" "))
    P = input()

    for i in arreglo:
        if P == "0" and i % 2 == 0:
            print(i, end=" ")
        elif P == "1" and i % 2 != 0:
            print(i, end=" ")


if __name__ == '__main__':
    _main()
