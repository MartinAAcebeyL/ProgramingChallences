#
from typing import List


def findRelativeRanks(score: List[int]) -> List[str]:
    sorted_score = sorted(score, reverse=True)
    size_score = len(score)
    values_dict = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(
        map(str, range(4, size_score + 1))
    )
    positions_dict = dict(zip(sorted_score, values_dict))
    answer = [positions_dict.get(sco) for sco in score]

    return answer


print(findRelativeRanks([5, 4, 3, 2, 1]))
print(findRelativeRanks([10, 3, 8, 9, 4]))
