import numpy as np

day = "14"
input = open("2023/inputs/day" + day + ".txt").read().strip().splitlines()
lines = [list(x) for x in input]
grid = np.array(lines)


def spin(new_grid):
    x_list, y_list = np.where(new_grid == "O")
    rocks = list(zip(x_list, y_list))
    for r, c in rocks:
        if r == 0:
            continue
        for i in range(r + 1):
            if new_grid[r - i - 1, c] in ("O", "#") or i == r:
                new_grid[r, c] = "."
                new_grid[r - i, c] = "O"
                break
    return new_grid


def solve(new_grid):
    ans = 0
    for i, row in enumerate(new_grid):
        ans += list(row).count("O") * (len(new_grid) - i)
    return ans


C = 42 * 2 + 34
new_grid = grid.copy()
for i in range(C):
    new_grid = spin(new_grid)
    new_grid = spin(new_grid.T).T
    new_grid = spin(new_grid[::-1])[::-1]
    new_grid = np.flip(spin(new_grid.T[::-1]).T, 1)


print(solve(spin(grid)), solve(new_grid))
