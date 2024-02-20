# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1


def duplicate_count(text: str) -> dict:
    text = text.lower()
    count = {}
    for char in text:
        count[char] = count.get(char, 0) + 1
    return count


string = input()
duplicates = duplicate_count(string)
counter = 0
for value in duplicates.values():
    if value > 1:
        counter += 1
print(counter)
