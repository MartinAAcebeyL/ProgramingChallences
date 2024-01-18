# url: https://codeforces.com/problemset/problem/200/B
n = int(input())
fractions = list(map(int, input().split()))

min_fraction = min(fractions)

average_fraction = sum(fractions) / n

result = max(min_fraction, average_fraction)
print("{:.12f}".format(result))
