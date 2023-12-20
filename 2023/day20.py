import math
from collections import deque
from functools import reduce

day = "20"
input = open("2023/inputs/day" + day + ".txt").read().strip().splitlines()
lines = [x.replace(" ", "").split("->") for x in input]


def reset():
    flipflop = dict()
    conjunction = dict()
    for line in lines:
        if line[0] == "broadcaster":
            broadcaster = line[1].split(",")
        elif line[0][0] == "%":
            flipflop[line[0][1:]] = ["off", line[1].split(",")]
        elif line[0][0] == "&":
            conjunction[line[0][1:]] = [{}, line[1].split(",")]
    for mod, outputs in flipflop.items():
        for x in outputs[1]:
            if x in conjunction:
                conjunction[x][0][mod] = "low"
    for mod, outputs in conjunction.items():
        for x in outputs[1]:
            if x in conjunction:
                conjunction[x][0][mod] = "low"
    return flipflop, conjunction, broadcaster


def pushbutton(broadcaster, flipflop, conjunction, find_node):
    high, low = 0, 1
    q = deque()
    for bc in broadcaster:
        q.append((bc, "low", "broadcaster"))
        low += 1

    while len(q) > 0:
        module, signal, input = q.popleft()
        if module in flipflop:
            if signal == "high":
                continue
            elif flipflop[module][0] == "off":
                flipflop[module][0] = "on"
                for x in flipflop[module][1]:
                    q.append((x, "high", module))
                    high += 1
            elif flipflop[module][0] == "on":
                flipflop[module][0] = "off"
                for x in flipflop[module][1]:
                    q.append((x, "low", module))
                    low += 1

        elif module in conjunction:
            conjunction[module][0][input] = signal
            if len(set(conjunction[module][0].values())) == 1 and signal == "high":
                for x in conjunction[module][1]:
                    q.append((x, "low", module))
                    low += 1
            else:
                for x in conjunction[module][1]:
                    q.append((x, "high", module))
                    high += 1
                if module == find_node:
                    return flipflop, conjunction, high, low, True

    return flipflop, conjunction, high, low, False


C = 1000
high_pulses = 0
low_pulses = 0
flipflop, conjunction, broadcaster = reset()
for i in range(C):
    flipflop, conjuction, high, low, _ = pushbutton(broadcaster, flipflop, conjunction, "DUMMY")
    high_pulses += high
    low_pulses += low


try_list = []
for con in conjuction:
    if "rx" in conjuction[con][1]:
        special_node = con
for con in conjuction:
    if special_node in conjuction[con][1]:
        try_list.append(con)

cycle_list = []
for try_node in try_list:
    found = False
    i = 0
    flipflop, conjunction, broadcaster = reset()
    while found == False:
        flipflop, conjuction, high, low, found = pushbutton(
            broadcaster, flipflop, conjunction, try_node
        )
        i += 1
    cycle_list.append(i)


print(high_pulses * low_pulses)
print(reduce(lambda x, y: math.lcm(x, y), cycle_list))
