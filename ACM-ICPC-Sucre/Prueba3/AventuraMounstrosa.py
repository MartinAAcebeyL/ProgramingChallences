N = int(input())
numeros = list(map(int, input().split()))

estado = 0
anterior = numeros[0]
correct = True

for i in numeros[1:]:
    if estado == 0:
        if i > anterior:
            anterior = i
        elif i == anterior:
            estado = 1
            anterior = i
        else:
            estado = 1
            anterior = i
    elif estado == 1:
        if i < anterior:
            estado = 2
            anterior = i
        elif i == anterior:
            continue
        else:
            correct = False
            break
    elif estado == 2:
        if i >= anterior:
            correct = False
            break
        anterior = i

result = "YES" if correct else "NO"
print(result)
