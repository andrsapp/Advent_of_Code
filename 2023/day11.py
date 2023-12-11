import numpy as np

day = "11"
input = open("2023/inputs/day" + day + ".txt").read().strip().splitlines()
lines = np.array([list(x) for x in input])

row_idx = []
for i, line in enumerate(lines):
    if "#" not in line:
        row_idx.append(i)

col_idx = []
for i, line in enumerate(lines.T):
    if "#" not in line:
        col_idx.append(i)

x_list, y_list = np.where(lines == "#")
coords = tuple(zip(x_list, y_list))


def solve(C):
    ans = 0
    for i, coord1 in enumerate(coords):
        next = i + 1
        for coord2 in coords[next:]:
            y1, x1 = coord1
            y2, x2 = coord2
            y_gal = sum([y in range(min(y1, y2) + 1, max(y1, y2)) for y in row_idx])
            x_gal = sum([x in range(min(x1, x2) + 1, max(x1, x2)) for x in col_idx])
            ans += abs(y1 - y2) + abs(x1 - x2) + y_gal * C + x_gal * C - y_gal - x_gal
    return ans


print(solve(2), solve(1000000))
