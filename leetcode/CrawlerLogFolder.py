# url: https://leetcode.com/problems/crawler-log-folder/description/?envType=daily-question&envId=2024-07-10

from typing import List


def minOperations(logs: List[str]) -> int:
    # ["d1/","d2/","../","d21/","./"]
    place = 0
    for log in logs:
        if log.startswith("../"):
            place = -1
        elif not log.startswith("."):
            place = +1
    return place
