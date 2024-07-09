# url: https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
import random


def modifyString(self, s: str) -> str:
    ABC = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
    r = ""
    for index, char in enumerate(s):
        if char == "?":
            excluded = set()
            if index > 0:
                excluded.add(r[index - 1])
            if index < len(s) - 1:
                excluded.add(s[index + 1])
            r += random.choice(list(ABC - excluded))
        else:
            r += char
    return r