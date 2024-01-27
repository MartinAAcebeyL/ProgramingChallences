# url: https://www.codewars.com/kata/5526fc09a1bbd946250002dc

numbers = [int(x) for x in input().split()]


even_numbers = 0  # pares
odd_numbers = 0

las_even_number = 0
las_odd_number = 0

is_even_numbers = False
for number in numbers:
    if number % 2 == 0:
        las_even_number = number
        even_numbers += 1
    else:
        las_odd_number = number
        odd_numbers += 1

    if (odd_numbers > 1 and even_numbers > 0) or (even_numbers > 1 and odd_numbers > 0):
        break


if odd_numbers > 1:
    print(las_even_number)
print(las_odd_number)
