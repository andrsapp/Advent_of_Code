import re
from collections import deque

day = "19"
input = open("2023/inputs/day" + day + ".txt").read().strip().split("\n\n")
lines = [x.splitlines() for x in input]

lines1 = [re.split(",|{|}", x.replace("}", "")) for x in lines[0]]
workflows = dict()
for line in lines1:
    workflows[line[0]] = line[1:]

ratings = [[int(y) for y in re.sub("{|x|m|a|s|=|}", "", x).split(",")] for x in lines[1]]

xmas_dict = {"x": 0, "m": 1, "a": 2, "s": 3}


def calc_step(rule, ratings):
    for w in workflows[rule][:-1]:
        condition, new_workflow = w.split(":")
        rating = ratings[xmas_dict[w[0]]]
        if eval(str(rating) + condition[1:]):
            return new_workflow
    return workflows[rule][-1]


ans_list = []
for r in ratings:
    rule = "in"
    while True:
        rule = calc_step(rule, r)
        if rule == "A":
            ans_list.append(sum(r))
            break
        elif rule == "R":
            break

print(sum(ans_list))


approve_list = []
q = deque()
q.append(("in", []))

while len(q) > 0:
    node, conditions = q.popleft()

    if node == "A":
        approve_list.append(conditions)
        continue
    elif node == "R":
        continue

    cond_list = []
    for i, branch in enumerate(workflows[node]):
        if i == 0:
            pass
        else:
            cond_list[i - 1] = "!" + cond_list[i - 1]

        if i == len(workflows[node]) - 1:
            new_node = branch
        else:
            new_condition, new_node = branch.split(":")
            cond_list.append(new_condition)
        q.append((new_node, conditions + cond_list))

ans = 0
for cond_list in approve_list:
    xmas_minmax = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    for cond in cond_list:
        if cond[0] == "!":
            cat = cond[1]
            sign = cond[2]
            value = int(cond[3:])
            cat_min, cat_max = xmas_minmax[cat]
            if sign == ">":
                xmas_minmax[cat] = (cat_min, min(value, cat_max))
            elif sign == "<":
                xmas_minmax[cat] = (max(cat_min, value), cat_max)
        else:
            cat = cond[0]
            sign = cond[1]
            value = int(cond[2:])
            cat_min, cat_max = xmas_minmax[cat]
            if sign == "<":
                xmas_minmax[cat] = (cat_min, min(value - 1, cat_max))
            elif sign == ">":
                xmas_minmax[cat] = (max(cat_min, value + 1), cat_max)
    combos = 1
    for val in xmas_minmax.values():
        combos *= val[1] - val[0] + 1
    ans += combos

print(ans)
