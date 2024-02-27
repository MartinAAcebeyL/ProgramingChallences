# url: https://codeforces.com/problemset/problem/4/C
n = int(input())

names = {}
for _ in range(n):
    name = input()
    if name in names:
        print(name + str(names[name]))
    else:
        print("OK")
    names[name] = names.get(name, 0) + 1
