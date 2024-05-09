# url: https://leetcode.com/problems/maximize-happiness-of-selected-children/description/?envType=daily-question&envId=2024-05-09
from typing import List


def maximumHappinessSum(happiness: List[int], k: int) -> int:
    happiness.sort(reverse=True)
    index, counter = 0, 0
    for _ in range(k):
        if happiness[index] - index > 0:
            counter += happiness[index] - index
            index += 1
    return counter


print(maximumHappinessSum([1, 2, 3], 2))  # 4
print(maximumHappinessSum([1, 1, 1, 1], 2))  # 1
print(maximumHappinessSum([2, 3, 4, 5], 1))  # 5
