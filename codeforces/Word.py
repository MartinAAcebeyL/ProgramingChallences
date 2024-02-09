# url: https://codeforces.com/problemset/problem/59/A
s = input()

lower_counter = 0
upper_counter = 0
s_size = len(s)

for char in s:
    if s_size // 2 + 1 in [lower_counter, upper_counter]:
        break
    if char.islower():
        lower_counter += 1
    else:
        upper_counter += 1

if lower_counter > upper_counter:
    print(s.lower())
elif lower_counter < upper_counter:
    print(s.upper())
else:
    print(s.lower())
