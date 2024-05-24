# url: https://leetcode.com/problems/rearrange-characters-to-make-target-string/description/


def count_words_on_target(s: str, target: str):
    d: dict = {}

    for i in s:
        if i in target:
            d[i] = d.get(i, 0) + 1
    return d


def rearrangeCharacters(s: str, target: str) -> int:
    c = 0
    finish = False
    words_dict = count_words_on_target(s, target)
    print(words_dict)

    while True:
        for i in target:
            if i not in words_dict.keys(): return 0
            if words_dict.get(i) == 0:
                finish = True
                break
            words_dict[i] = words_dict.get(i) - 1
        if finish:
            break
        c += 1
    return c

# s = "ilovecodingonleetcode"
# target = "code"
# print(rearrangeCharacters(s,target))

# s = "abbaccaddaeea"
# target = "aaaaa"
# print(rearrangeCharacters(s, target))

# s = "abcba"
# target = "abc"
# print(rearrangeCharacters(s, target))

s = "abc"
target = "abcd"
print(rearrangeCharacters(s, target))
