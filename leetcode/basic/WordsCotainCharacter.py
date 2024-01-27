from typing import List


words = ["leet", "code"]
x = "e"


def find_words_containing(words: List[str], x: str) -> List[int]:
    return [index for index, word in enumerate(words) if x in word]
