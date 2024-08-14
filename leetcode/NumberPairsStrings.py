# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

from typing import List


def numOfPairs(nums: List[str], target: str) -> int:
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(n):
            if i != j and nums[i] + nums[j] == target:
                count += 1

    return count


print(numOfPairs(nums=["777", "7", "77", "77"], target="7777"))
print(numOfPairs(nums=["123", "4", "12", "34"], target="1234"))
print(numOfPairs(nums=["1", "1", "1"], target="11"))
