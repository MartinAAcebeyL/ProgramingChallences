
def get_mediana(N:int, L:int):
    if N % 2 == 0:
        return (L[N//2] + L[(N//2) + 1]) / 2
    return L[N//2]


if __name__ == "__main__":
    N = int(input())
    L = [int(x) for x in input().split()].sort()
    print(get_mediana(N, L))