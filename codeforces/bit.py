amount = int(input())

x = 0
for _ in range(amount):
    if "-" in input():
        x -= 1
    else:
        x += 1

print(x)