def count_letters(word: str) -> list:
    r = {}
    for c in word:
        r[c] = r.get(c, 0) + 1
    return list(r.values())


s = input()
count = 0
array = count_letters(s)


def minimun_deletions(index: int) -> bool:
    global count
    aux = False
    for _index, i in enumerate(array):
        if _index == index or array[index] == 0:
            continue
        if array[index] == i:
            array[index] -= 1
            count += 1
            aux = True
    return aux


index = 0
while True:
    if index == len(array) - 1:
        break
    if minimun_deletions(index):
        pass
    else:
        index += 1

print(count)
