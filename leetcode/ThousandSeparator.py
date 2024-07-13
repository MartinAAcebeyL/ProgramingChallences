# url: https://leetcode.com/problems/thousand-separator/

def thousandSeparator(n: int) -> str:
    if n == 0:
        return '0'
    res = ''
    i = 0
    while n:
        if i == 3:
            res = '.' + res
            i = 0
        res = str(n % 10) + res
        n //= 10
        i += 1
    return res