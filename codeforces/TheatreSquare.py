# url: https://codeforces.com/problemset/problem/1/A

import math

n, m, a = [int(x) for x in input().split()]

num_flagstones = math.ceil(n / a) * math.ceil(m / a)

print(num_flagstones)
