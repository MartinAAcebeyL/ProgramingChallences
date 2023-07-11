def check_diference(listado: list) -> bool:
    for i in range(len(listado)-1):
        if listado[i]-listado[i+1] != 10:
            return False
    return True


listado = list(map(int, input().split()))
print(check_diference(listado))
