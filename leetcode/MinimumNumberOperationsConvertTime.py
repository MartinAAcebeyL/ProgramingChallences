# url: https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/description/
from datetime import datetime


def get_minutes(current: str, correct: str) -> int:
    fmt = "%H:%M"
    # Convertir las cadenas de tiempo a objetos datetime
    dt_current = datetime.strptime(current, fmt)
    dt_correct = datetime.strptime(correct, fmt)

    # Obtener la diferencia en minutos
    minutos = (dt_correct - dt_current).total_seconds() / 60

    return int(minutos)


def convertTime(current: str, correct: str) -> int:
    minutes = get_minutes(current, correct)
    operations = 0
    for increment in [60, 15, 5, 1]:
        operations += minutes // increment
        minutes %= increment
    
    return operations


current = "02:30"
correct = "04:35"
# print(convertTime(current, correct))
current = "11:00"
correct = "11:01"
# print(convertTime(current, correct))
print(convertTime("00:00", "23:59"))
