# url: https://leetcode.com/problems/sum-of-square-numbers/?envType=daily-question&envId=2024-06-17
from math import sqrt


def judgeSquareSum(c: int) -> bool:
    a, b = 0, int(sqrt(c))
    while a <= b:
        s = a**2 + b**2
        if s == c:
            return True
        if s < c:
            a += 1
        else:
            b -= 1
    return False
