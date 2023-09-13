
numero = int(input())


numero_volteado = 0
es_negativo = False

if numero < 0:
    es_negativo = True
    numero = numero*-1

while numero > 0:
    digito = numero % 10
    numero_volteado = numero_volteado * 10 + digito
    numero //= 10

if es_negativo:
    numero_volteado = -numero_volteado


if numero_volteado < pow(2,31)*-1  or numero_volteado > pow(2,31)-1:
    print(0)
else:
    print(numero_volteado)
