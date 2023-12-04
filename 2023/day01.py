import re

num_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
num_dict = dict()
for i, num in enumerate(num_list):
    num_dict[num] = str(i + 1)
num_list.extend([str(x) for x in range(1, 10)])


def part1(lines):
    ans = 0
    for line in lines:
        line = re.sub("[^0-9]", "", line)
        ans += 10 * int(line[0]) + int(line[-1])
    return ans


def part2(lines):
    ans = 0
    for line in lines:
        # first digit
        num_first = "0"
        curr_pos = 99
        for num in num_list:
            pos = line.find(num)
            if pos != -1 and pos < curr_pos:
                curr_pos = pos
                num_first = num
        if num_first.isnumeric() is False:
            num_first = num_dict[num_first]

        # second digit
        num_second = "0"
        curr_pos = -2
        for num in num_list:
            pos = max([x.start() for x in re.finditer(num, line)] + [-1])
            if pos != -1 and pos > curr_pos:
                curr_pos = pos
                num_second = num
        if num_second.isnumeric() is False:
            num_second = num_dict[num_second]

        ans += 10 * int(num_first) + int(num_second)
    return ans


def main():
    day = "01"
    input = open("2023/inputs/day" + day + ".txt").read().strip()
    lines = input.split("\n")
    print(part1(lines), part2(lines))


if __name__ == "__main__":
    main()
