from typing import List

nums = [1, 2, 3, 4]


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n
    suffix_product = 1

    for i in range(1, n):
        result[i] = result[i - 1] * nums[i - 1]

    for i in range(n - 1, -1, -1):
        result[i] *= suffix_product
        suffix_product *= nums[i]

    return result


print(product_except_self(nums))
