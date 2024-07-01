# url: https://leetcode.com/problems/three-consecutive-odds/description/?envType=daily-question&envId=2024-07-01
from typing import List


def threeConsecutiveOdds(arr: List[int]) -> bool:
    counter = 0
    for num in arr:
        if num % 2 != 0:
            counter += 1
        else:
            counter = 0
        if counter > 2:
            break
    return counter == 3
