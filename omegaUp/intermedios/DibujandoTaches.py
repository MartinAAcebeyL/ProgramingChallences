
def draw_tache(n: int) -> str:
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print("@", end="")
            else:
                print(" ", end="")
        if i != n-1:
            print()


if __name__ == "__main__":
    dimension = int(input())
    draw_tache(dimension)
