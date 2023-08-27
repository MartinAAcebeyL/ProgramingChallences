def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def max_pairwise_gcd(numbers):
    n = len(numbers)
    max_gcd = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_gcd = max(max_gcd, gcd(numbers[i], numbers[j]))
    return max_gcd

N = int(input())

for _ in range(N):
    numbers = list(map(int, input().split()))
    
    result = max_pairwise_gcd(numbers)
    print(result)
