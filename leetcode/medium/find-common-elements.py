# url: https://leetcode.com/problems/find-common-elements-between-two-arrays/description/

from typing import List, Dict


def make_dictionary(l: List[int]) -> Dict:
    apparition_dictionary = {}
    for number in l:
        apparition_dictionary[number] = apparition_dictionary.get(number, 0) + 1
    return apparition_dictionary


def find_intersection_values(nums1: List[int], nums2: List[int]) -> List[int]:
    dict_num1 = make_dictionary(nums1)
    dict_num2 = make_dictionary(nums2)
    r1, r2 = 0, 0

    for value in dict_num1:
        if dict_num1.get(value) and dict_num2.get(value):
            r1 += dict_num1.get(value)
            r2 += dict_num2.get(value)
    return [r1, r2]


nums1 = [4, 3, 2, 3, 1]
nums2 = [2, 2, 5, 2, 3, 6]
print(find_intersection_values(nums1, nums2))
