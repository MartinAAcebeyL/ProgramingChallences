# url: https://codeforces.com/problemset/problem/231/A
n = int(input())

problems_solved = 0
for _ in range(n):
    problems = input().split()
    if problems.count("1") >= 2:
        problems_solved += 1
print(problems_solved)
