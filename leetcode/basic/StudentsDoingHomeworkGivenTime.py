# url: https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/description/

from typing import List


def busy_student(startTime: List[int], endTime: List[int], queryTime: int) -> int:
    counter = 0
    for i_st, i_et in zip(startTime, endTime):
        if i_st<=queryTime and i_et>=queryTime:
            counter += 1
    return counter


def busy_student_1(startTime: List[int], endTime: List[int], queryTime: int) -> int:
    return sum(start <= queryTime <= end for start, end in zip(startTime, endTime))
