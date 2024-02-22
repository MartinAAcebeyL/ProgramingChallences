def is_almost_lucky(n):
    lucky_numbers = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]
    for lucky_num in lucky_numbers:
        if n % lucky_num == 0:
            return "YES"
    return "NO"


n = int(input())
print(is_almost_lucky(n))
