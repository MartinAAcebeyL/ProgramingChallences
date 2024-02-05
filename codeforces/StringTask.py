# url: https://codeforces.com/problemset/problem/118/A
string = input()

lower_vowels = "aeiouy"
upper_vowels = "AEIOUY"

r = ""
for char in string:
    if char in lower_vowels or char in upper_vowels:
        continue
    if char.isupper():
        char = char.lower()
    r += f".{char}"

print(r)
