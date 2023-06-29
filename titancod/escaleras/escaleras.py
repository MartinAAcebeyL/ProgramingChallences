def maxima_altura(pilas):
    suma = sum(pilas)
    for i in range(1, len(pilas)+1):
        suma_aux = sum(range(1, i+1))
        if suma == suma_aux:
            return i


c = int(input())  
contarador_array = []

for _ in range(c):
    pilas = list(map(int, input().split()))

    altura_maxima = maxima_altura(pilas)
    contador = 0  

    for pila in pilas:
        diferencia = altura_maxima - pila  
        contador += diferencia  

    contarador_array.append(contador)

for contador in contarador_array:
    print(contador)
