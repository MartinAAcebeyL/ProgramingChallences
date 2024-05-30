# url: https://leetcode.com/problems/count-asterisks/description/


def countAsterisks(s: str) -> int:
    separate = s.split("|")
    s = 0
    for index, char in enumerate(separate):
        if (index + 1) % 2 != 0:
            s += char.count("*")
    return s


print(countAsterisks("l|*e*et|c**o|*de|"))  # 2
print(countAsterisks("iamprogrammer"))  # 0
print(countAsterisks("yo|uar|e**|b|e***au|tifu|l"))  # 5
