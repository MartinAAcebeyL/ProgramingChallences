n = int(input())
groups = list(map(int, input().split()))

counts = [0] * 5
for group in groups:
    counts[group] += 1

taxis = counts[4]

taxis += counts[3]
counts[1] = max(
    0, counts[1] - counts[3]
)

taxis += counts[2] // 2
counts[2] %= 2

if counts[2]:
    taxis += 1
    counts[1] = max(
        0, counts[1] - 2
    ) 

taxis += (counts[1] + 3) // 4

print(taxis)
