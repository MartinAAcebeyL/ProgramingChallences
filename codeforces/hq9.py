# url: https://codeforces.com/problemset/problem/133/A
hq9 = input()

is_posible = False
for char in hq9:
    if char in ("H", "Q", "9"):
        is_posible = True
        break

print("YES" if is_posible else "NO")
