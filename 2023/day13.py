import numpy as np

day = "13"
input = open("2023/inputs/day" + day + ".txt").read().strip().split("\n\n")
lines = [[list(y) for y in x.splitlines()] for x in input]
lines = [np.array(x) for x in lines]


def get_reflect(pattern, k, hor, part):
    matches = []
    for i, row1 in enumerate(pattern):
        for j, row2 in enumerate(pattern[i + 1 :]):
            if all(row1 == row2) is True:
                matches.append((i, i + 1 + j))
            if sum(row1 == row2) == len(row1) - 1 and part == 2:
                matches.append((i, i + 1 + j))
    reflect_pts = []
    for match in matches:
        if part == 1:
            if match[1] - match[0] == 1:
                reflect_pts.append(match)
        else:
            if match[1] - match[0] == 1 and not (match == ref_list[k] and hor == flag_list[k]):
                reflect_pts.append(match)
    if reflect_pts == []:
        return (False, (-99999, -99999))
    for reflect in reflect_pts:
        flag = False
        i, j = reflect
        if i == 0 or j == len(pattern) - 1:
            return (True, reflect)
        while flag is False:
            i -= 1
            j += 1
            if (i, j) not in matches:
                break
            if i == 0 or j == len(pattern) - 1:
                return (True, reflect)
    return (False, (-1, -1))


p1 = 0
ref_list = []
flag_list = []
for k, pattern in enumerate(lines):
    hor_flag, ref_line = get_reflect(pattern, 0, 0, 1)
    if hor_flag is False:
        hor_flag, ref_line = get_reflect(pattern.T, 0, 0, 1)
        p1 += ref_line[1]
        flag_list.append(False)
    else:
        p1 += 100 * ref_line[1]
        flag_list.append(True)
    ref_list.append(ref_line)


p2 = 0
for k, pattern in enumerate(lines):
    hor_flag, ref_line = get_reflect(pattern, k, True, 2)
    if hor_flag is False:
        hor_flag, ref_line = get_reflect(pattern.T, k, False, 2)
        p2 += ref_line[1]
    else:
        p2 += 100 * ref_line[1]

print(p1, p2)
