# url: https://leetcode.com/problems/arranging-coins/description/
class Solution:
    def arrangeCoins(self, n: int) -> int:
        table_size, increse_by = self.makeTableGame(n)
        print(increse_by)
        return increse_by - 1

    def makeTableGame(self, n: int) -> int:
        table_size = 1
        incresse_by = 2
        while table_size <= n:
            table_size += incresse_by
            incresse_by += 1
        return table_size, incresse_by - 1
