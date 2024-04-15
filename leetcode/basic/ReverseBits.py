# url: https://leetcode.com/problems/reverse-bits/?source=submission-ac

def reverse_bits(self, n: int) -> int:
    binary_str = bin(n)[2:].zfill(32)
    reversed_n = int(binary_str[::-1], 2)
    return reversed_n
