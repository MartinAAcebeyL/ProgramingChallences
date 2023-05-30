
def hora_palindroma(hora: list) -> str:
    hora_aux = []
    for i in hora:
        hora_aux.append(i[::-1])
    return "SI" if hora == hora_aux[::-1] else "NO"


if __name__ == "__main__":
    data = []
    while True:
        hora = input().split(" ")
        if hora == ["0", "0"]:
            break
        data.append(hora)
        
    for hora in data:
        print(hora_palindroma(hora))
