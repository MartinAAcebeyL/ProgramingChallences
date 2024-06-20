# url: https://leetcode.com/problems/number-of-1-bits/
def hammingWeight(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
