n = abs(int(input()))
limit = 0
for i in range(1,n+1):
  limit+=i

print(int((limit * (limit + 1)) / 2))