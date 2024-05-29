# url: https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/description/

from typing import List


def sum_digits_on_array(n: List[int]) -> int:
    s = 0
    for i in n:

        if i <= 9:
            s += i
        else:
            while i > 0:
                s += i % 10
                i //= 10
    return s


def differenceOfSum(nums: List[int]) -> int:
    sum_elements = sum(nums)
    sum_by_digits = sum_digits_on_array(nums)

    return abs(sum_elements - sum_by_digits)


print(differenceOfSum([1, 15, 6, 3]))  # 9
print(differenceOfSum([1, 2, 3, 4]))  # 0
