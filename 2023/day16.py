from collections import deque

import numpy as np

day = "16"
input = open("2023/inputs/day" + day + ".txt").read().strip().splitlines()
lines = [list(x) for x in input]
m = np.array(lines)

R, C = np.shape(m)

# up, down, left, right
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

slash_dict = {0: [3, 2], 1: [2, 3], 2: [1, 0], 3: [0, 1]}


# returns dr, dc index
def get_reflect(tile, dir):
    if tile == ".":
        return [dir]
    elif tile == "/":
        return [slash_dict[dir][0]]
    elif tile == "\\":
        return [slash_dict[dir][1]]
    elif tile == "-" and dir in (2, 3):
        return [dir]
    elif tile == "|" and dir in (0, 1):
        return [dir]
    elif tile == "-" and dir in (0, 1):
        return [2, 3]
    elif tile == "|" and dir in (2, 3):
        return [0, 1]


def beam(sr, sc, sd):
    energized = np.full((R, C, 4), ".")

    rq, cq, dq = deque(), deque(), deque()

    rq.append(sr)
    cq.append(sc)
    dq.append(sd)

    while len(rq) > 0:
        r, c, d = rq.popleft(), cq.popleft(), dq.popleft()

        energized[r, c, d] = "#"

        dir_list = get_reflect(m[r, c], d)
        for index in dir_list:
            rr = r + dr[index]
            cc = c + dc[index]

            if rr < 0 or cc < 0:
                continue
            if rr >= R or cc >= C:
                continue
            if energized[rr, cc, index] == "#":
                continue

            rq.append(rr)
            cq.append(cc)
            dq.append(index)

    return len(set(zip(list(np.where(energized == "#")[0]), list(np.where(energized == "#")[1]))))


ans_list = []
for j in range(R):
    for sd in range(4):
        if sd == 0:
            sr, sc = R - 1, j
        elif sd == 1:
            sr, sc = 0, j
        elif sd == 2:
            sr, sc = j, C - 1
        elif sd == 3:
            sr, sc = j, 0

        ans_list.append(beam(sr, sc, sd))

p1 = beam(0, 0, 3)
p2 = max(ans_list)

print(p1, p2)
