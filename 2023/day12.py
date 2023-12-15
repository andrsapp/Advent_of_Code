day = "12"
input = open("2023/inputs/day" + day + ".txt").read().strip().splitlines()
lines = [x.split() for x in input]
lines = [[a, b.split(",")] for a, b in lines]


def get_state_dict(s, spring, pat_dict, pattern, dif_length, springs):
    state_dict = dict()
    for state, prev_cnt in pat_dict.items():
        for i, record in enumerate(pattern):
            if i < state:
                continue
            if i >= sum(springs[: s + 1]) + s + dif_length:
                continue
            if "#" in pattern[state:i]:
                break
            before = pattern[0:i]
            chunk = pattern[i : i + spring + 2]
            after = pattern[i + spring + 2 :]
            if "." not in chunk[1:-1] and "#" not in (chunk[0], chunk[-1]) and "x" not in chunk:
                new = before + "." + "x" * (spring) + "." + after
                if "#" in after and s == len(springs) - 1:
                    continue
                if new.rfind("x") + 1 in state_dict:
                    state_dict[new.rfind("x") + 1] += 1 * prev_cnt
                else:
                    state_dict[new.rfind("x") + 1] = 1 * prev_cnt
    return state_dict


def solve(part):
    ans = 0
    for p, o in lines[0:]:
        if part == 1:
            p2 = "?".join([p])
            o2 = ",".join([",".join(o)])
        else:
            p2 = "?".join([p for x in range(5)])
            o2 = ",".join([",".join(o) for x in range(5)])
        left_pattern = "." + ".".join(p2.replace(".", " ").split()) + "..."
        springs = [int(x) for x in o2.split(",")]
        dif_length = len(left_pattern) - (sum(springs) + len(springs) + 1)

        pat_dict = {0: 1}
        for s, spring in enumerate(springs[0:]):
            pat_dict = get_state_dict(s, spring, pat_dict, left_pattern, dif_length, springs)
        ans += sum(pat_dict.values())
    return ans


print(solve(1), solve(2))
