# url: https://codeforces.com/problemset/problem/69/A


def is_equilibrium(forces):
    sum_x = sum_y = sum_z = 0
    for x, y, z in forces:
        sum_x += x
        sum_y += y
        sum_z += z
    return "YES" if sum_x == sum_y == sum_z == 0 else "NO"


n = int(input())
forces = []
for _ in range(n):
    force = list(map(int, input().split()))
    forces.append(force)

print(is_equilibrium(forces))
