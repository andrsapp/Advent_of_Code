import re

red = 12
green = 13
blue = 14


def solve(lines):
    ans_p1 = 0
    ans_p2 = 0
    for line in lines:
        blue_max = 0
        red_max = 0
        green_max = 0
        for i, item in enumerate(line):
            if i == 0:
                continue
            ball = item.split()
            for j, x in enumerate(ball):
                x = re.sub(",", "", x).strip()
                if j == 0:
                    continue
                if x == "blue":
                    blue_max = max(blue_max, int(ball[j - 1]))
                elif x == "red":
                    red_max = max(red_max, int(ball[j - 1]))
                elif x == "green":
                    green_max = max(green_max, int(ball[j - 1]))
        if blue_max <= blue and red_max <= red and green_max <= green:
            ans_p1 += int(line[0].split()[1])
        ans_p2 += blue_max * red_max * green_max
    return (ans_p1, ans_p2)


def main():
    day = "02"
    input = open("2023/inputs/day" + day + ".txt").read().strip().split("\n")
    lines = [re.split(":|;", line) for line in input]
    print(solve(lines))


if __name__ == "__main__":
    main()
