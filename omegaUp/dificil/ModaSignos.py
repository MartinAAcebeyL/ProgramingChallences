# url: https://omegaup.com/arena/problem/La-moda-y-sus-signos/


if __name__ == "__main__":
    cantidad_numeros = input()
    numeros = list(map(int, input().split()))

    diccionario_numeros = {}
    for numero in numeros:
        num_abs = abs(numero)
        if num_abs not in diccionario_numeros:
            diccionario_numeros[num_abs] = 1
        else:
            diccionario_numeros[num_abs] += 1

    maximo = 0
    clave = 0
    for i, j in diccionario_numeros.items():
        if j > maximo:
            maximo = j
            clave = i
        elif j == maximo and i < clave: 
            clave = i

    print(clave)
    print(numeros.count(clave), diccionario_numeros.get(
        clave)-numeros.count(clave))
