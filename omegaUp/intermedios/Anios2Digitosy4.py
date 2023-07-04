# url: https://omegaup.com/arena/problem/Anyos-con-dos-y-cuatro-digitos/

def convertir_a_4_digitos(anio: int) -> str:
    if int(anio) >= 74 and int(anio) <= 99:
        return f"{dia}/{mes}/19{anio}"
    return f"{dia}/{mes}/20{anio}"


UAM_ANIO = 1974
if __name__ == "__main__":
    while True:
        fecha = input().split("/")
        if fecha == ['']:
            break
        dia, mes, anio = fecha
        print(convertir_a_4_digitos(int(anio)))
