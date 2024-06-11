# url: https://leetcode.com/problems/relative-sort-array/description/?envType=daily-question&envId=2024-06-11
from typing import List


def relativeSortArray(arr1: List[int], arr2: List[int]) -> List[int]:
    new_array = []
    uniques = []
    index_array = []
    for val_2 in arr2:
        for index, val_1 in enumerate(arr1):
            if val_1 == val_2:
                new_array.append(val_1)
            elif val_1 not in arr2 and index not in index_array:
                uniques.append(val_1)
                index_array.append(index)
    return new_array + uniques.sort()


print(relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))
print(relativeSortArray([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]))
