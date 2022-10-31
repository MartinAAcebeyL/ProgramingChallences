#add two numbers

intentos = int(input())
for _ in range(intentos):
    try:
        (a, b) = map(int, input().split(' '))
    except Exception as e:
        print(e)
        continue
    suma = a + b
    print(suma)