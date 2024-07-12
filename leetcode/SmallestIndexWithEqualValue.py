# url: https://leetcode.com/problems/smallest-index-with-equal-value/
from typing import List


def smallestEqual(nums: List[int]) -> int:
    for index, num in enumerate(nums):
        if index%10==num:
            return index
    return -1