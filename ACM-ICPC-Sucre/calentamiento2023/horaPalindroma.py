def hora_palindroma(hora: str) -> str:
    return "SI" if hora == hora[::-1] else "NO"


if __name__ == "__main__":
    while True:
        hora = input().split()
        if hora[0] == "0" and hora[1] == "0":
            break
        print(hora_palindroma("".join(hora)))
