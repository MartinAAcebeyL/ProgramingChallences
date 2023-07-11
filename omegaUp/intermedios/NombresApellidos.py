# url: https://omegaup.com/arena/problem/Nombres-y-apellidos-sanos/
import sys


def check_name(name: list) -> str:
    name_count = len(name)
    if name_count == 1 or name_count > 4:
        return "*"
    if name_count == 3:
        name_count = 4

    return f"{ ' '.join(name[name_count//2:]) } {' '.join(name[:name_count//2])}"


if __name__ == "__main__":
    for line in sys.stdin:
        print(check_name(line.split()))
