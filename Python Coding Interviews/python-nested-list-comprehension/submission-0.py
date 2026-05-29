from typing import List


def create_grid(rows: int, cols: int, value: int) -> List[List[int]]:
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(value)
        matrix.append(row)
    return matrix

# do not modify below this line
print(create_grid(2, 3, 0))
print(create_grid(3, 2, 1))
print(create_grid(4, 4, 4))
print(create_grid(1, 1, 5))
print(create_grid(1, 5, 5))
