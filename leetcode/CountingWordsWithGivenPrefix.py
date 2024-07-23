# url: https://leetcode.com/problems/counting-words-with-a-given-prefix/description/

from typing import List
def prefixCount(words: List[str], pref: str) -> int:
    return sum(1 for word in words if word.startswith(pref))