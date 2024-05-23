# url: https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

from typing import List


def make_dictionary(l: list) -> dict:
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1
    return d


def numberOfPairs(nums: List[int]) -> List[int]:
    frecuency_numbers: dict = make_dictionary(nums)
    pairs, leftover = 0, 0
    for i in frecuency_numbers:
        pairs += frecuency_numbers.get(i) // 2
        leftover += frecuency_numbers.get(i) % 2

    return [pairs, leftover]


# print(numberOfPairs([1, 3, 2, 1, 3, 2, 2]))  # 3,1
print(numberOfPairs([1, 1]))  # 1, 1
# print(numberOfPairs([0]))  # 0,1
