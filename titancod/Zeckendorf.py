# url: https://www.titancod.net/problema/REPZE

def fibonacci(n: int = 109) -> list:
    fib_list = [0, 1]
    while len(fib_list) < n:
        next_number = fib_list[-1] + fib_list[-2]
        fib_list.append(next_number)
    return fib_list


PRIMOS = fibonacci(40)

number = int(input())


while number != 0:
    for i in PRIMOS[::-1]:
        if i <= number:
            number -= i
            print(i, end=" ")
            break
print()