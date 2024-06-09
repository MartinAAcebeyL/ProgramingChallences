# url: https://leetcode.com/problems/count-the-digits-that-divide-a-number/description/


def countDigits(num: int) -> int:
    copy = num
    counter = 0
    resto = num % 10
    while resto > 0:
        if copy % resto == 0:
            counter += 1
        num = num // 10
        resto = num % 10
    return counter


print(countDigits(7))  # 1
print(countDigits(121))  # 2
print(countDigits(1248))  # 4
