# url: https://leetcode.com/problems/single-number-iii/description/?envType=daily-question&envId=2024-05-31
from typing import List


def singleNumber(nums: List[int]) -> List[int]:
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1

    return sorted(d, key=lambda x: d.get(x))[:2]


print(singleNumber([1, 2, 1, 3, 2, 5]))
print(singleNumber([-1, 0]))
print(singleNumber([0, 1]))
