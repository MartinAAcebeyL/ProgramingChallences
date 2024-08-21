# url: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

from typing import List
from collections import Counter


def countCharacters(words: List[str], chars: str) -> int:
    chars_count = Counter(chars)
    counter = 0
    for word in words:
        if Counter(word) <= chars_count:
            counter += len(word)
    return counter


print(countCharacters(words=["cat", "bt"], chars="atach"))
