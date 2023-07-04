# url:https://omegaup.com/arena/problem/Comparando-numero-de-galaxias/

if __name__ == "__main__":
    a, b, c = list(map(int, input().split(" ")))
    print(a < b, c > a, a == b, a != c, c <= b)
