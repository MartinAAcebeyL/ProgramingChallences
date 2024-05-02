# url: https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/?envType=daily-question&envId=2024-05-02

from typing import List


def findMaxK(nums: List[int]) -> int:
    sorted_nums = sorted(nums)
    number_to_return = -1
    i = 0

    while sorted_nums[i] < 0:
        num = sorted_nums[i]
        if abs(num) in sorted_nums:
            number_to_return = abs(num)
            break
        i += 1
        if i >= len(nums): break

    return number_to_return


print(findMaxK([-1, 2, -3, 3]))  # 3
print(findMaxK([-1, 10, 6, 7, -7, 1]))  # 7
print(findMaxK([-10, 8, 6, 7, -2, -3]))  # -1
print(findMaxK([-30]))  # -1
