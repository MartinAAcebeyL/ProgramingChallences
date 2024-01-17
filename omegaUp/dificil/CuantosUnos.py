# url: https://omegaup.com/arena/problem/Cuantos-Unos/

n = int(input())
binary_representation = bin(n)[2:]
print(binary_representation.count("1"))
