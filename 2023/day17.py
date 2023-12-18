import sys
from queue import PriorityQueue

import numpy as np

day = "17"
input = open("2023/inputs/day" + day + ".txt").read().strip().splitlines()
lines = [list(x) for x in input]
m = np.array(lines).astype(int)

R, C = np.shape(m)

sr, sc = 0, 0

# up, down, left, right
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def dijkstra(m, sr, sc, part):
    visited = np.full((R, C, 4), False)

    prev = dict()
    for r in range(R):
        for c in range(C):
            for i in range(4):
                prev[(r, c, i)] = (-1, -1, -1)

    dist = np.full((R, C, 4), sys.maxsize)
    dist[sr, sc, 1] = 0
    dist[sr, sc, 3] = 0

    pq = PriorityQueue()
    pq.put((0, (sr, sc, 1)))
    pq.put((0, (sr, sc, 3)))

    while pq.empty() is False:
        min_value, (r, c, d) = pq.get()
        visited[r, c, d] = True
        if dist[r, c, d] < min_value:
            continue

        for i in range(0, 4):
            if d == i:
                continue
            elif d == 0 and i == 1:
                continue
            elif d == 1 and i == 0:
                continue
            elif d == 2 and i == 3:
                continue
            elif d == 3 and i == 2:
                continue

            if part == 1:
                for plus in range(3):
                    rr = r + dr[i] * (plus + 1)
                    cc = c + dc[i] * (plus + 1)

                    if rr < 0 or cc < 0:
                        continue
                    if rr >= R or cc >= C:
                        continue

                    if visited[rr, cc, i]:
                        continue

                    if plus == 0:
                        new_dist = dist[r, c, d] + m[r + dr[i], c + dc[i]]
                    elif plus == 1:
                        new_dist = (
                            dist[r, c, d]
                            + m[r + dr[i], c + dc[i]]
                            + m[r + dr[i] * 2, c + dc[i] * 2]
                        )
                    elif plus == 2:
                        new_dist = (
                            dist[r, c, d]
                            + m[r + dr[i], c + dc[i]]
                            + m[r + dr[i] * 2, c + dc[i] * 2]
                            + m[r + dr[i] * 3, c + dc[i] * 3]
                        )

                    if new_dist < dist[rr, cc, i]:
                        prev[(rr, cc, i)] = (r, c, d)
                        dist[rr, cc, i] = new_dist
                        pq.put((new_dist, (rr, cc, i)))

            if part == 2:
                for plus in range(4, 11):
                    rr = r + dr[i] * (plus)
                    cc = c + dc[i] * (plus)

                    if rr < 0 or cc < 0:
                        continue
                    if rr >= R or cc >= C:
                        continue

                    if visited[rr, cc, i]:
                        continue

                    new_dist = dist[r, c, d]
                    for j in range(1, plus + 1):
                        new_dist += m[r + dr[i] * j, c + dc[i] * j]

                    if new_dist < dist[rr, cc, i]:
                        prev[(rr, cc, i)] = (r, c, d)
                        dist[rr, cc, i] = new_dist
                        pq.put((new_dist, (rr, cc, i)))

    return dist, prev


# Unecessary for final answer, but very useful for debugging
def find_shortest_path(m, sr, sc, er, ec):
    _, prev = dijkstra(m, sr, sc, 2)
    at = (er, ec, 1)
    path = [at]
    while at[0:2] != (-1, -1):
        at = prev[at]
        path.append(at)
    path.reverse()
    return path[1:]


dist_p1, _ = dijkstra(m, sr, sc, 1)
dist_p2, _ = dijkstra(m, sr, sc, 2)

print(min(dist_p1[R - 1, C - 1, 1], dist_p1[R - 1, C - 1, 3]))
print(min(dist_p2[R - 1, C - 1, 1], dist_p2[R - 1, C - 1, 3]))
