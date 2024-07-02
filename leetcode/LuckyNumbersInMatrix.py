# url: https://leetcode.com/problems/lucky-numbers-in-a-matrix/
from typing import List


def luckyNumbers(matrix: List[List[int]]) -> List[int]:
    lucky_numbers = []
    # min on row and max on column

    for row in matrix:
        min_number_on_row = min(row)
        index_min_number = row.index(min_number_on_row)
        array_column = []
        for _row in matrix:
            array_column.append(_row[index_min_number])
        if min_number_on_row == max(array_column):
            lucky_numbers.append(min_number_on_row)
    return lucky_numbers


print(luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))  # 15
print(luckyNumbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))  # 12
print(luckyNumbers([[7, 8], [1, 2]]))  # 7
