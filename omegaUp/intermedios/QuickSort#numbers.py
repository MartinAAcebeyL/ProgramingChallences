from typing import List


def quicksort(z: List[int]):
    if len(z) > 1:
        piv = int(len(z) / 2)
        val = z[piv]
        lft = [i for i in z if i > val]
        mid = [i for i in z if i == val]
        rgt = [i for i in z if i < val]
        res = quicksort(lft) + mid + quicksort(rgt)
        return res
    else:
        return z


n = int(input())
numbers = list(map(int, input().split()))
print(*quicksort(numbers)[:3], sep="\n")
