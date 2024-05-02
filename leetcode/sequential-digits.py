# url: https://leetcode.com/problems/sequential-digits/description/?envType=daily-question&envId=2024-02-02

from typing import List


def sequential_digits(low: int, high: int) -> List[int]:
    result = []

    for i in range(1, 10):
        num = i
        while num <= high:
            if low <= num <= high:
                result.append(num)
            last_digit = num % 10
            if last_digit == 9:
                break
            num = num * 10 + (last_digit + 1)
    return sorted(result)


low = 100
high = 300

print(sequential_digits(low, high))
