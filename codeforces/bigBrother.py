# url: https://codeforces.com/problemset/problem/791/A

weight_limak, weight_bob = map(int, input().split())

years = 0

while True:
    weight_limak *= 3
    weight_bob *= 2
    years += 1
    if weight_limak > weight_bob:
        break

print(years)
