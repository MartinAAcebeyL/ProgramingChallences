# url: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/submissions/1271900933/
from typing import List


def findTheDistanceValue(arr1: List[int], arr2: List[int], d: int) -> int:
    distance_value = 0

    for a in arr1:
        is_distant = True
        for b in arr2:
            if abs(a - b) <= d:
                is_distant = False
                break
        if is_distant:
            distance_value += 1

    return distance_value
