def create_pascal_triangle(num_rows: int) -> list[list[int]]:
    if num_rows == 1:
        return [[1]]
    elif num_rows == 2:
        return [[1], [1, 1]]

    pascal_triangle = [[1], [1, 1]]

    for _ in range(3, num_rows + 1):
        last_row = pascal_triangle[-1]
        aux = []
        for j in range(len(last_row)-1):
            aux.append(last_row[j] + last_row[j+1])
        aux.insert(0, 1)
        aux.append(1)
        pascal_triangle.append(aux)
    return pascal_triangle


num_rows = int(input())
print(create_pascal_triangle(num_rows))
