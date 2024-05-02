nums = [int(i) for i in input().split(',')]
target = int(input())
len_nums = len(nums)

encontrado = False
for i in range(len_nums-1):
    for j in nums[i+1:]:
        if j >= target:
            continue

        if nums[i]+j == target:
            print(f"[{i}, {nums.index(j,i)}]")
            encontrado = True
            break
    if encontrado:
        break
