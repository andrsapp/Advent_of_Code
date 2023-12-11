import random

import numpy as np

day = "10"
input = open("2023/inputs/day" + day + ".txt").read().strip().splitlines()
lines = [list(x) for x in input]
m = np.array(lines)

R, C = len(m), len(m[0])
sr, sc = np.where(m == "S")[0][0], np.where(m == "S")[1][0]
rq, cq = [], []

visited = np.full((R, C), False)

# up, down, left, right
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

pipe_list = []

rq.append(sr)
cq.append(sc)
pipe_list.append((sr, sc))
visited[sr, sc] = True


def p1solve():
    move_count = 0
    nodes_left = 1
    nodes_next = 0

    while len(rq) > 0:
        r = rq.pop(0)
        c = cq.pop(0)

        # CHECK NEIGHBORS
        for i in range(0, 4):
            rr = r + dr[i]
            cc = c + dc[i]

            if rr < 0 or cc < 0:
                continue
            if rr >= R or cc >= C:
                continue

            if visited[rr, cc]:
                continue

            # logic
            if i == 0 and m[rr, cc] not in ("F", "7", "|"):
                continue
            elif i == 1 and m[rr, cc] not in ("J", "L", "|"):
                continue
            elif i == 2 and m[rr, cc] not in ("-", "F", "L"):
                continue
            elif i == 3 and m[rr, cc] not in ("-", "J", "7"):
                continue
            elif m[r, c] == "|" and i in (2, 3):
                continue
            elif m[r, c] == "-" and i in (0, 1):
                continue
            elif m[r, c] == "F" and i in (0, 2):
                continue
            elif m[r, c] == "7" and i in (0, 3):
                continue
            elif m[r, c] == "J" and i in (1, 3):
                continue
            elif m[r, c] == "L" and i in (1, 2):
                continue

            rq.append(rr)
            cq.append(cc)
            pipe_list.append((rr, cc))

            visited[rr, cc] = True
            nodes_next += 1

        # END CHECK NEIGHBORS

        nodes_left -= 1
        if nodes_left == 0:
            nodes_left = nodes_next
            nodes_next = 0
            move_count += 1
    return move_count


print(p1solve() - 1)

sr, sc = 0, 0
rq, cq = [], []

visited = np.full((R, C), False)
for pipe in pipe_list:
    visited[pipe[0], pipe[1]] = True

# up, down, left, right
dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, -1, 1, 1, -1]

out_set = set()
in_set = []
in_set_all = set()
for row in range(R):
    for col in range(C):
        if visited[row, col]:
            continue
        else:
            temp_set = {(row, col)}
            outside = False
            visited[row, col] = True

            rq.append(row)
            cq.append(col)

            while len(rq) > 0:
                r = rq.pop(0)
                c = cq.pop(0)

                # CHECK NEIGHBORS
                for i in range(0, 8):
                    rr = r + dr[i]
                    cc = c + dc[i]

                    if rr < 0 or cc < 0:
                        outside = True
                        continue
                    if rr >= R or cc >= C:
                        outside = True
                        continue

                    if visited[rr, cc]:
                        continue

                    rq.append(rr)
                    cq.append(cc)

                    visited[rr, cc] = True
                    temp_set.add((rr, cc))

            if outside is True:
                out_set.update(temp_set)
            else:
                in_set.append(temp_set)
                in_set_all.update(temp_set)

# changed based on input
m[sr, sc] = "J"

ans = 0
for coords in in_set:
    coord = random.choice(tuple(coords))
    r, c = coord
    cnt = 0
    for i in range(c):
        if (r, c - i - 1) in out_set:
            break
        if (r, c - i - 1) in in_set_all:
            continue
        if m[r, c - i - 1] == "|":
            cnt += 1
            continue
        if m[r, c - i - 1] == "7":
            curr = "7"
        elif m[r, c - i - 1] == "J":
            curr = "J"
        elif m[r, c - i - 1] == "F":
            if curr == "7":
                cnt += 2
            elif curr == "J":
                cnt += 1
            curr = ""
        elif m[r, c - i - 1] == "L":
            if curr == "7":
                cnt += 1
            elif curr == "J":
                cnt += 2
            curr = ""
    if cnt % 2 == 1:
        ans += len(coords)
print(ans)
