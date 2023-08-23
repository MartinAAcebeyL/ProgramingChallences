if __name__ == "__main__":
    columns, arrows = map(int, input().split())

    counter = {}
    for _ in range(arrows):
        valor = map(int, input().split())
        for i in valor:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
    diccionario_ordenado = dict(sorted(counter.items()))
    for i in diccionario_ordenado.values():
        if i == 0:
            continue
        print(i, end=" ")
