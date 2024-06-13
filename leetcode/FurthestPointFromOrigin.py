# url: https://leetcode.com/problems/furthest-point-from-origin/description/


def furthestDistanceFromOrigin(moves: str) -> int:
    l, r = moves.count("L"), moves.count("R")
    lines = len(moves) - (l + r)

    if l > r:
        return l + lines - r
    elif r > l or l==r:
        return r + lines - l
    


print(furthestDistanceFromOrigin("L_RL__R"))  # 3
print(furthestDistanceFromOrigin("_R__LL_"))  # 5
print(furthestDistanceFromOrigin("_______"))  # 7
