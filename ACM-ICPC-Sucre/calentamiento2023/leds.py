def calcular_leds(hh, mm):
    digitos = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    hora = hh * 100 + mm
    leds = sum(digitos[int(digito)] for digito in str(hora))
    max_leds = int('1' * (leds // 2))
    return leds, hora, max_leds


n = int(input())
aux = []
for _ in range(n):
    hh, mm = map(int, input().split())
    aux.append([hh, mm])
    
for i in aux:
    hh, mm = i
    leds, hora, max_leds = calcular_leds(hh, mm)  # Calcular resultados
    print(leds)
    print(hora)
    print(max_leds)
