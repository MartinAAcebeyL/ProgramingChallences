# url:https://omegaup.com/arena/problem/Elevando-al-cuadrado-UAM/
LIMITE = 30000

if __name__ == "__main__":
    N = int(input())
    contador = 0
    while N < LIMITE:
        N = N**2
        contador += 1
    print(f"{N} {contador}")
