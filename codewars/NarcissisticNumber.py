def narcissistic(value):
    str_value = str(value)
    size_value = len(str_value)
    total = sum(int(digit) ** size_value for digit in str_value)
    return total == value


print(narcissistic(1938))
