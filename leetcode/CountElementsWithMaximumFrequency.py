# url: https://leetcode.com/problems/count-elements-with-maximum-frequency/description/

from typing import List
from collections import Counter


def maxFrequencyElements(nums: List[int]) -> int:
    nums_dict = getDicctionary(nums)
    first_value = next(iter(nums_dict.values()))
    sum_max_frequency = sum(filter(lambda x: x == first_value, nums_dict.values()))
    return sum_max_frequency


def getDicctionary(elements: List[int]) -> dict[int:int]:
    counter = Counter(elements)
    sorted_counter = dict(counter.most_common())
    return sorted_counter


print(maxFrequencyElements([1, 2, 2, 3, 1, 4]))
print(maxFrequencyElements([1, 2, 3, 4, 5]))
