# url: https://www.codewars.com/kata/567c26df18e9b1083a000049/train/python


def last_man_standing(n):
    numbers = list(range(2, n + 1, 2))
    eliminate_left = False

    while len(numbers) > 1:
        if eliminate_left:
            numbers = numbers[1::2]
        else:
            numbers = numbers[-2::-2][::-1]

        eliminate_left = not eliminate_left

    return numbers[0]
