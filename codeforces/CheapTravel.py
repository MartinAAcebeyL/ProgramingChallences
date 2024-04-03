# url: https://codeforces.com/problemset/problem/466/A

n, m, a, b = map(int, input().split())

money = 0

division = n // m
resto = n % m

first_method = (division + 1) * b if resto else division * b
second_method = n * a
third_method = resto * a + division * b if resto else b * division

print(min(first_method, second_method, third_method))
