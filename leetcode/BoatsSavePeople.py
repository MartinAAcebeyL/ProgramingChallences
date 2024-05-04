from typing import List


def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort()
    boats = 0
    left, right = 0, len(people) - 1

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1

    return boats


print(numRescueBoats([1, 2], 3))  # 1
print(numRescueBoats([3, 2, 2, 1], 3))  # 3
print(numRescueBoats([3, 5, 3, 4], 5))  # 4
print(numRescueBoats([5, 1, 4, 2], 6))  # 2
