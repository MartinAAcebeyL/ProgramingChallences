# url: https://leetcode.com/problems/clear-digits/description/


def clearDigits(s: str) -> str:
    new_s = ""

    for char in s:
        if char.isdecimal():
            new_s = new_s[:-1]
        else:
            new_s += char
    return new_s

print(clearDigits("abc"))
print(clearDigits("cb34"))
