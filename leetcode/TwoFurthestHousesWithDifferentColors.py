# url: https://leetcode.com/problems/two-furthest-houses-with-different-colors/

from typing import List


def maxDistance(colors: List[int]) -> int:
    first_house = colors[0]
    last_house = colors[-1]
    s, s1 = None, None
    c, c1 = 0, 0

    for color in range(len(colors)):

        if colors[color] != first_house:
            s = c
        if last_house != colors[-color - 1]:
            s1 = c1
        c += 1
        c1 += 1
    return max(s, s1)
