# # url: https://codeforces.com/problemset/problem/58/A

TARGET = "hello"


def can_say_hello(s: str) -> str:
    index_target = 0

    for char in s:
        if index_target > 4:
            break
        if char == TARGET[index_target]:
            index_target += 1

    if index_target == 5:
        return "YES"
    return "NO"


s = input()
print(can_say_hello(s))
