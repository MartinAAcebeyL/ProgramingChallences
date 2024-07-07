# url: https://leetcode.com/problems/water-bottles/description/?envType=daily-question&envId=2024-07-07
def numWaterBottles(numBottles: int, numExchange: int) -> int:
    r = numBottles
    while numBottles >= numExchange:
        r += numBottles // numExchange
        numBottles = numBottles // numExchange + numBottles % numExchange
    return r
