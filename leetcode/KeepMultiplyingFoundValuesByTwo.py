# url: https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/

from typing import List


def findFinalValue(nums: List[int], original: int) -> int:

    while original in nums:
        original *= 2
    return original
