def extraer_signo_numero(number: int):
    if number < 0:
        return "-", abs(number)
    return "+", number


def convert_to_string(polinomio: list[int]) -> str:
    formatted_terms = []
    grado = 8
    for i in polinomio:
        if i == 0 and grado != 0:
            grado -= 1
            continue
        signo, number = extraer_signo_numero(i)
        char = ''
        if not formatted_terms:
            char += f"{i}x^{grado}"if number != 1 else f"x^{grado}"
        elif grado > 1:
            char += f" {signo} {number}x^{grado}"if number != 1 else f" {signo} x^{grado}"
        elif grado == 1:
            char += f" {signo} {number}x"if number != 1 else f" {signo} x"
        else:
            char += f" {signo} {number}"if number != 0 else f""

        grado -= 1

        formatted_terms.append(char)

    return ''.join(formatted_terms)


cases = int(input())
outputs = []
for _ in range(cases):
    polinomio = list(map(int, input().split()))
    outputs.append(convert_to_string(polinomio))

for i in outputs:
    print(i)
