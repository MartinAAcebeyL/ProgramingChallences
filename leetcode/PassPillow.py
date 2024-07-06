# url: https://leetcode.com/problems/pass-the-pillow/description/?envType=daily-question&envId=2024-07-06


def passThePillow(n: int, time: int) -> int:
    cycle_length = 2 * (n - 1)
    effective_time = time % cycle_length
    
    if effective_time < n:
        return effective_time + 1
    return 2 * n - effective_time - 1


print(passThePillow(4, 5))  # 2
print(passThePillow(3, 2))  # 3
print(passThePillow(18, 38))  # 5
print(passThePillow(15, 400))  # 9
