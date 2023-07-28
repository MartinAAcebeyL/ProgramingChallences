import sys


def decifrar_codigo_chim_pun(number: int) -> int:
    if number ==2:
        return 3
    
    potencia = 0
    while 3**potencia<number:
        potencia+=1
    
    return number+3**potencia


if __name__ == "__main__":
    for number in sys.stdin:
        print(decifrar_codigo_chim_pun(int(number)))
