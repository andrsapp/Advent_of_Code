import re

day = "15"
input = open("2023/inputs/day" + day + ".txt").read().strip().split(",")
lines = [re.split("=|-", x) for x in input]


def HASH(pattern):
    cur_value = 0
    for char in pattern:
        cur_value += ord(char)
        cur_value *= 17
        cur_value %= 256
    return cur_value


p1 = 0
for line in input:
    p1 += HASH(line)

lens_dict = dict()
for i in range(256):
    lens_dict[i] = dict()
for lens, focal in lines:
    if focal == "":
        if lens in lens_dict[HASH(lens)].keys():
            lens_dict[HASH(lens)].pop(lens)
    else:
        lens_dict[HASH(lens)][lens] = int(focal)

p2 = 0
for box_num, box in lens_dict.items():
    for i, (lens, focal) in enumerate(box.items()):
        p2 += (1 + box_num) * (i + 1) * focal

print(p1, p2)
