import sys


def convert_match(velocidad: int) -> float:
    _match = (velocidad * 1000/3600)/340
    return _match


for velocidad in sys.stdin:
    resultado = int(convert_match(int(velocidad)) * 10) / 10
    print(resultado)