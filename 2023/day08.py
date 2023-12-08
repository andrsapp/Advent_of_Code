import math
import re
from functools import reduce


def find_Z(elem, instruct, node_dict):
    steps = 0
    while elem.endswith("Z") is False:
        for dir in instruct:
            if dir == "L":
                elem = node_dict[elem][0]
            elif dir == "R":
                elem = node_dict[elem][1]
            steps += 1
            if elem.endswith("Z"):
                return steps
    return -1


def main():
    day = "08"
    input = open("2023/inputs/day" + day + ".txt").read().strip().splitlines()
    instruct = input[0]
    lines = [re.sub("[^A-Z]", " ", x) for x in input[2:]]

    node_dict = dict()
    for line in lines:
        node, left, right = line.split()
        node_dict[node] = (left, right)

    elem = "AAA"
    steps = 0
    while elem != "ZZZ":
        for dir in instruct:
            if dir == "L":
                elem = node_dict[elem][0]
            elif dir == "R":
                elem = node_dict[elem][1]
            steps += 1
            if elem == "ZZZ":
                break
    p1 = steps

    start_list = []
    for item in node_dict.keys():
        if item.endswith("A"):
            start_list.append(item)
    step_list = []
    for elem in start_list:
        step_list.append(find_Z(elem, instruct, node_dict))

    p2 = reduce(lambda x, y: math.lcm(x, y), step_list)

    print(p1, p2)


if __name__ == "__main__":
    main()
