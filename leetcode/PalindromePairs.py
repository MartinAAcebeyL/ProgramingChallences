# url: https://leetcode.com/problems/palindrome-pairs/
from typing import List


def palindromePairs(words: List[str]) -> List[List[int]]:
    index_palindromic = []
    size_words = len(words)
    word_map = {word: i for i, word in enumerate(words)}

    print(word_map)
    for i in range(size_words - 1):
        i_word = words[i]
        for j in range(i + 1, size_words):
            i_concat = i_word + words[j]
            j_concat = words[j] + i_word

            if i_concat == i_concat[::-1]:
                index_palindromic.append([i, j])
            if j_concat == j_concat[::-1]:
                index_palindromic.append([j, i])
    return index_palindromic


print(
    palindromePairs(words=["abcd", "dcba", "lls", "s", "sssll"])
)  # [[0,1],[1,0],[3,2],[2,4]]
