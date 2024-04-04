# url: https://codeforces.com/problemset/problem/339/B

n, m = map(int, input().split())
homes = map(int, input().split())

time_to_complete_all_tasks = 0
current_home = 1

for home in homes:
    is_behind = home - current_home < 0
    time_to_complete_all_tasks += (
        home - current_home + n if is_behind else home - current_home
    )
    current_home = home

print(time_to_complete_all_tasks)
