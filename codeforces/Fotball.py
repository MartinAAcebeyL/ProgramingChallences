# url: https://codeforces.com/problemset/problem/43/A
n = int(input())

play = []
for _ in range(n):
    play.append(input())

player_1_win = False

if play.count(play[0]) > n // 2:
    player_1_win = True
    print(play[0])
else:
    player_2_win = list(filter(lambda p: p != play[0], play))
    print(player_2_win[0])
