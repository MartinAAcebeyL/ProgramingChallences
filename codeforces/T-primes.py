import math


def generate_primes_sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve


PRIME_SIEVE = generate_primes_sieve(1000000)


def is_t_prime(num):
    sqrt_num = int(math.sqrt(num))
    return sqrt_num * sqrt_num == num and PRIME_SIEVE[sqrt_num]


# Input
n = int(input())
numbers = map(int, input().split())

for num in numbers:
    if is_t_prime(num):
        print("YES")
    else:
        print("NO")
