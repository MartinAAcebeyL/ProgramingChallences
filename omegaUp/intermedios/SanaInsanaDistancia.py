# url: https://omegaup.com/arena/problem/Sana-o-insana-distancia/

from math import sqrt


def is_sana_distance(numbers: list) -> str:
    distance = sqrt((numbers[0] - numbers[2])**2 +
                    (numbers[1] - numbers[3])**2)

    return "sana" if distance >= 150 else "insana"


if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    print(is_sana_distance(numbers))
