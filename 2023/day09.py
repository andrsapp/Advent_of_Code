day = "09"
input = open("2023/inputs/day" + day + ".txt").read().strip().splitlines()
lines = [x.split() for x in input]
lines = [[int(x) for x in line] for line in lines]


def next_seq(num_list):
    pattern = []
    for i in range(len(num_list) - 1):
        pattern.append(num_list[i + 1] - num_list[i])
    return pattern


p1 = 0
for line in lines:
    last_num = [line[-1]]
    pattern = line
    while sum(pattern) != 0:
        pattern = next_seq(pattern)
        last_num.append(pattern[-1])
    p1 += sum(last_num)

p2 = 0
for line in lines:
    last_num = [line[0]]
    pattern = line
    while sum(pattern) != 0:
        pattern = next_seq(pattern)
        last_num.append(pattern[0])
    last_num.reverse()
    x = 0
    for i, num in enumerate(last_num[1:]):
        x = num - x
    p2 += x

print(p1, p2)
