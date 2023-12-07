# url: https://codeforces.com/problemset/problem/71/A

n = int(input())

for _ in range(n):
    s = input()
    string = s
    if len(s) > 10:
        string = f"{s[0]}{len(s)-2}{s[-1]}"
    print(string)
