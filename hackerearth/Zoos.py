# url: https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/is-zoo-f6f309e7/

word = input()
z = word.count('z')
o = word.count('o')
if z*2 == o:
    print("Yes")
else:
    print("No")
