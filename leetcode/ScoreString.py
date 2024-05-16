# url: https://leetcode.com/problems/score-of-a-string/description/
def scoreOfString(s: str) -> int:
    size = len(s) - 1
    c = 0
    for i in range(size):
        c += abs(ord(s[i]) - ord(s[i + 1]))

    return c


print(scoreOfString("hello"))
print(scoreOfString("zaz"))
print(scoreOfString("za"))
