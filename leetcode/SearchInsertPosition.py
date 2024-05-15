# url: https://leetcode.com/problems/search-insert-position/submissions/1258299922/
from typing import List


def search_insert(nums: List[int], target: int) -> int:
    start, end = 0, len(nums) - 1

    while start <= end:
        middle = (start + end) // 2
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            end = middle - 1
        elif nums[middle] < target:
            start = middle + 1
    return start
