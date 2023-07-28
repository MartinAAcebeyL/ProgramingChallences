# url: https://www.titancod.net/problema/CICLISTA


def calculate_speed(speed: list, travel: list) -> float:
    upload_speed, normal_speed, lowering_speed = speed
    upload_travel = travel.count(-1) * 5
    normal_travel = travel.count(0) * 5
    lowering_travel = travel.count(1) * 5

    t = upload_travel/upload_speed+normal_travel / \
        normal_speed+lowering_travel/lowering_speed

    return round(t, 1)


if __name__ == "__main__":
    test_cases = int(input())

    for test_case in range(test_cases):
        speed_travel = [int(i) for i in input().split()]
        travel = [int(i) for i in input().split()]

        print(calculate_speed(speed_travel[:-1], travel))
