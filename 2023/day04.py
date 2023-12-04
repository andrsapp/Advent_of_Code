import re


def get_match(lines):
    ans = 0
    match_list = []
    for line in lines:
        winners = set(line[1].split())
        mine = set(line[2].split())
        both = winners.intersection(mine)
        if len(both) > 0:
            ans += 2 ** (len(both) - 1)
        match_list.append(len(both))
    return (ans, match_list)


def main():
    day = "04"
    input = open("2023/inputs/day" + day + ".txt").read().strip().split("\n")
    lines = [re.split(":|\\|", x) for x in input]
    ans, match_list = get_match(lines)

    card_list = [1 for x in range(len(match_list))]
    for i, num in enumerate(match_list):
        if num == 0:
            continue
        for j in range(num):
            if i + j + 1 >= len(card_list):
                continue
            card_list[i + j + 1] += card_list[i]
    print(ans, sum(card_list))


if __name__ == "__main__":
    main()
