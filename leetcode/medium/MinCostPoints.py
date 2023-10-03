points = [[3, 12], [-2, 5], [-4, 1]]
len_points = len(points)
conections = [-1]*len_points


def calculate_min_distance_manhatan(_index, point):
    min_distance = float('inf')
    for index, i in enumerate(points):
        if i == point:
            continue
        distance_manhatan = abs(i[0]-point[0])+abs(i[1]-point[1])
        if distance_manhatan < min_distance:
            min_distance = distance_manhatan
            conections[_index] = index
            if conections[conections[_index]] == _index:
                min_distance -= distance_manhatan

    return min_distance


_min_distance = 0
for index, point in enumerate(points):
    a = calculate_min_distance_manhatan(index, point)
    _min_distance += a
print(_min_distance)
