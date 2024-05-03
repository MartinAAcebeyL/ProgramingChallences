# url: https://leetcode.com/problems/compare-version-numbers/description/?envType=daily-question&envId=2024-05-03

from itertools import zip_longest

def compareVersion(version1: str, version2: str) -> int:
    array_version1 = list(map(int, version1.split(".")))
    array_version2 = list(map(int, version2.split(".")))

    is_version1_bigger = 0
    for num1, num2 in zip_longest(array_version1, array_version2, fillvalue=0):
        if num1 > num2:
            is_version1_bigger = 1
            break
        elif num2 > num1:
            is_version1_bigger = -1
            break
    return is_version1_bigger


print(compareVersion("1.01", "1.001"))  # 0
print(compareVersion("1.0", "1.0.0"))  # 0
print(compareVersion("0.1", "1.1"))  # -1
print(compareVersion("7.5.2.4", "7.5.3")) # -1
print(compareVersion("1.0.1", "1"))  # 1
