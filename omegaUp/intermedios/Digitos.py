N = int(input())

cadena = ''.join(map(str, range(1, N+1)))

print(cadena.index(str(N)) + 1)
