# url: https://leetcode.com/problems/find-maximum-number-of-string-pairs/description/
from typing import List
from collections import Counter


# def maximumNumberOfStringPairs(words: List[str]) -> int:
#     word_size = len(words)
#     counter = 0
#     for i in range(word_size):
#         i_word = words[i]
#         for j in range(i + 1, word_size):
#             if i_word == words[j][::-1]:
#                 counter += 1
#     return counter


def maximumNumberOfStringPairs(words: List[str]) -> int:
    seen = []
    counter = 0
    for word in words:
        reverse_word = word[::-1]
        if reverse_word in seen:
            counter += 1
        seen.append(word)
    return counter


print(maximumNumberOfStringPairs(["cd", "ac", "dc", "ca", "zz"]))
