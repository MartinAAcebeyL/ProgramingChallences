# https://codeforces.com/problemset/problem/1352/C
amount = int(input())
for _ in range(amount):
    n, k = map(int, input().split())
    print(k + (k - 1) // (n - 1))