# url: https://www.codewars.com/kata/550f22f4d758534c1100025a/train/python


OPPOSITES = {
    "NORTH": "SOUTH",
    "SOUTH": "NORTH",
    "EAST": "WEST",
    "WEST": "EAST",
}

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]


def dir_reduc(arr):
    stack = []

    for direction in arr:
        if stack and stack[-1] == OPPOSITES[direction]:
            stack.pop()
        else:
            stack.append(direction)

    return stack


print(dir_reduc(a))
