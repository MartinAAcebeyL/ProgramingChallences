# url:https://omegaup.com/arena/problem/Numeros-en-media-espiral/
N = int(input())

i = 1
n = N
print(i, end=" ")

count = 0
flag = False

for _ in range(N-1):
    if count >= 2:
        flag = not flag
        count = 0

    if flag:
        i += 1
        print(i, end=" ")
    else:
        print(n, end=" ")
        n -= 1

    count += 1
