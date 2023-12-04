import numpy as np

dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, 1, -1, -1, 1]


def get_parts(engine):
    R = engine.shape[0]
    C = engine.shape[1]
    numflag = False
    symbol = False
    parts = []
    row_id = []
    col_id = []
    for r in range(R):
        for c in range(C):
            if engine[r, c].isnumeric() is False:
                continue

            # check surroundings
            for i in range(0, 8):
                rr = r + dr[i]
                cc = c + dc[i]

                if rr < 0 or cc < 0:
                    continue
                if rr >= R or cc >= C:
                    continue

                if engine[rr, cc].isnumeric() is False and engine[rr, cc] != ".":
                    symbol = True
            # add number
            if numflag is False:
                num = engine[r, c]
                numflag = True
            else:
                num += engine[r, c]
            if c + 1 >= C or engine[r, c + 1].isnumeric() is False:
                numflag = False

            # append parts
            if numflag is False and symbol is True:
                parts.append(int(num))
                row_id.append(r)
                col_id.append([x for x in range(c - len(num) + 1, c + 1)])
                numflag = False
                symbol = False
    return parts, row_id, col_id


def main():
    day = "03"
    input = open("2023/inputs/day" + day + ".txt").read().strip().split("\n")
    lines = [list(x) for x in input]
    engine = np.array(lines)
    R = engine.shape[0]
    C = engine.shape[1]

    parts, row_id, col_id = get_parts(engine)
    coord_list = []
    for i, rr in enumerate(row_id):
        p = []
        for cc in col_id[i]:
            p.append((rr, cc))
        coord_list.append(p)

    ans = []
    for r in range(R):
        for c in range(C):
            if engine[r, c] != "*":
                continue
            adj_cnt = 0
            adj_list = []
            for p, row in enumerate(coord_list):
                found = False
                for x in row:
                    if found is True:
                        break
                    for i in range(0, 8):
                        rr = r + dr[i]
                        cc = c + dc[i]
                        if x == (rr, cc):
                            found = True
                            break
                if found is True:
                    adj_list.append(parts[p])
                    adj_cnt += 1
            if adj_cnt == 2:
                ans.append(adj_list)

    total = 0
    for x in ans:
        total += x[0] * x[1]
    print(sum(parts), total)


if __name__ == "__main__":
    main()
