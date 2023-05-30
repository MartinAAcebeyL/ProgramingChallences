def juego(A: int, B: int) -> str:
    if A == B:
        return "EMPATE"
    if A == 1:
        if B == 2:
            return "B"
        return "A"
    if A == 2:
        if B == 1:
            return "A"
        return "B"
    if A == 3:
        if B == 1:
            return "B"
        return "A"


if __name__ == "__main__":
    A = int(input())
    B = int(input())

    print(juego(A, B))
