# url: https://codeforces.com/problemset/problem/479/A


a = int(input())
b = int(input())
c = int(input())

expr1 = a + b + c
expr2 = a * b * c
expr3 = a + b * c
expr4 = a * (b + c)
expr5 = (a + b) * c

max_value = max(expr1, expr2, expr3, expr4, expr5)

print(max_value)
