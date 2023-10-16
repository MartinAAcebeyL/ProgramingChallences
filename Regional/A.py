def existe_subsegmento_mas_comun(n, k, a):
    max_count = 0
    current_count = 0
    for num in a:
        if num == k:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count > 0


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    a = list(map(int, input().split()))
    if existe_subsegmento_mas_comun(n, k, a):
        print("YES")
    else:
        print("NO")
