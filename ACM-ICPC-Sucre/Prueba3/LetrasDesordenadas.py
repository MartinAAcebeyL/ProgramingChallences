def contador_letras(cadena: str) -> dict:
    dict = {}

    for letra in cadena:
        if letra not in dict:
            dict[letra] = 1
        else:
            dict[letra] += 1
    return dict


PADAWAN = input()
YEDAY = input()
LETRAS = input()

if contador_letras(PADAWAN+YEDAY)==contador_letras(LETRAS):
    print("YES")
else:
    print("NO")
