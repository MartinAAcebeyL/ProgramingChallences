# url: https://leetcode.com/problems/find-the-maximum-achievable-number/


def maximum_achievable_x(num: int, t: int) -> int:
    return num + t * 2


num = 4
t = 1
print(maximum_achievable_x(num, t))
