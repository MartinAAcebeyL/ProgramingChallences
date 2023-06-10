DIGITOS = {
    '0': 6,
    '1': 2,
    '2': 5,
    '3': 5,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 3,
    '8': 7,
    '9': 6
}


def calcular_leds(hora: str) -> str:
    cantidad_leds = 0
    for i in hora:
        cantidad_leds += DIGITOS[i]

    if cantidad_leds % 2 == 0:
        return cantidad_leds, hora, '1' * (cantidad_leds // 2)
    maximo = '7'+'1' * (cantidad_leds // 2-1)
    return cantidad_leds, hora, maximo


n = int(input())
horas = []
for _ in range(n):
    hh, mm = input().split()
    if len(mm) == 1:
        mm = '0' + mm
    horas.append(hh+mm)

for i in horas:
    leds, hora, max_leds = calcular_leds(i)
    print(f'{leds}\n{hora}\n{max_leds}')
