# url: https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python
def get_separate_data(number: int):
    new_number = 1
    while number > 9:
        new_number *= number % 10
        number //= 10

    return new_number * number


def persistence(n):
    counter = 0
    while n > 9:
        n = get_separate_data(n)
        counter += 1
    return counter


print(persistence(999))
