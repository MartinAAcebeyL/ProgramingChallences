# url: https://www.codewars.com/kata/55c45be3b2079eccff00010f
numbers = {
    "1": "",
    "2": "",
    "3": "",
    "4": "",
    "5": "",
    "6": "",
    "7": "",
    "8": "",
    "9": "",
}


def order(string):
    if not string:
        return ""
    for char in string.split():
        for key in numbers:
            if key in char:
                numbers[key] = char
                break

    r = " ".join([numbers[key] for key in numbers if numbers[key] != ""])

    return r
