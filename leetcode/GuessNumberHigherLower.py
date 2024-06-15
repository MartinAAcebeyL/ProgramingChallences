# https://leetcode.com/problems/guess-number-higher-or-lower/
class Solution:
    def guessNumber(self, n: int) -> int:
        pick = n // 2
        i, f = 1, n
        guesso = guess(pick)
        while guesso != 0:
            if guesso == -1:
                f = pick - 1
            elif guesso == 1:
                i = pick + 1

            pick = (f + i) // 2
            guesso = guess(pick)

        return pick
