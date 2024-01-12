# url: https://leetcode.com/problems/determine-if-string-halves-are-alike/description/?envType=daily-question&envId=2024-01-12

from functools import reduce


class Solution:
    def is_vowel(self, char):
        return char.lower() in "aeiou"

    def halvesAreAlike(self, s: str) -> bool:
        size = len(s)
        vowels_a = reduce(
            lambda ac, letter: ac + 1 if self.is_vowel(letter) else ac,
            s[: size // 2],
            0,
        )
        vowels_b = reduce(
            lambda ac, letter: ac + 1 if self.is_vowel(letter) else ac,
            s[size // 2 :],
            0,
        )

        return vowels_a == vowels_b
