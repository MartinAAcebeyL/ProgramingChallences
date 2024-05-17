# url: https://leetcode.com/problems/longest-common-prefix/
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    letter_with_min_size = sorted(strs, key=lambda x: len(x))[0]
    index = -1
    is_finish = False
    for i in range(len(letter_with_min_size)):
        to_compare = letter_with_min_size[i]
        print("to_compare: ", to_compare)
        for j in range(len(strs)):
            print(f"strs[{j}][{i}]: ", strs[j][i])
            if strs[j][i] != to_compare:
                is_finish = True
                break
        print()
        if is_finish:
            break
        index = i
    print("index: ", index)

    if index >= 1:
        return letter_with_min_size[:index+1]
    elif index == 0:
        return letter_with_min_size[index]
    else:
        return ""


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(["a"]))
print(longestCommonPrefix(["cir", "car"]))
