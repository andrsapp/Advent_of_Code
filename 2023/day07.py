from functools import cmp_to_key

card_list = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_dict = dict()
for i, card in enumerate(card_list):
    card_dict[card] = i

part = 1


def getrank(hand):
    hand_dict = dict()
    for card in hand:
        if str(card_dict[card]) in hand_dict.keys():
            hand_dict[str(card_dict[card])] += 1
        else:
            hand_dict[str(card_dict[card])] = 1
    if 5 in hand_dict.values():
        rank = 0
    elif 4 in hand_dict.values():
        rank = 1
    elif 3 in hand_dict.values() and 2 in hand_dict.values():
        rank = 2
    elif 3 in hand_dict.values():
        rank = 3
    elif list(hand_dict.values()).count(2) == 2:
        rank = 4
    elif 2 in hand_dict.values():
        rank = 5
    else:
        rank = 6

    if "12" in hand_dict.keys() and part == 2:
        if rank == 0:
            pass
        elif rank in (1, 2):  # Full house and 4 of a kind turn into five of a kind
            rank = 0
        elif rank == 3:  # 3 of a kind
            rank = 1  # 4 of a kind
        elif rank == 4:  # two pair
            if hand_dict["12"] == 2:
                rank = 1  # 4 of a kind
            else:
                rank = 2  # full house
        elif rank == 5:  # pair
            rank = 3  # 3 of a kind
        elif rank == 6:  # nothing
            rank = 5  # one pair
    return rank


def compare_hands(hand1, hand2):
    hand1rank = getrank(hand1)
    hand2rank = getrank(hand2)
    if hand1rank < hand2rank:
        return 1
    elif hand1rank > hand2rank:
        return -1
    elif hand1rank == hand2rank:
        for i in range(5):
            if card_dict[hand1[i]] == card_dict[hand2[i]]:
                continue
            elif card_dict[hand1[i]] < card_dict[hand2[i]]:
                return 1
            else:
                return -1
    return 0


def solve(lines):
    bet_dict = dict()
    for line in lines:
        bet_dict[line[0]] = int(line[1])

    hand_list = []
    for line in lines:
        hand_list.append(line[0])
    sorter = cmp_to_key(compare_hands)
    hand_list.sort(key=sorter)

    ans = 0
    for i, hand in enumerate(hand_list):
        ans += bet_dict[hand] * (i + 1)
    return ans


def main():
    day = "07"
    input = open("2023/inputs/day" + day + ".txt").read().strip().splitlines()
    lines = [x.split() for x in input]

    p1 = solve(lines)

    card_list_2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    global card_dict
    card_dict = dict()
    for i, card in enumerate(card_list_2):
        card_dict[card] = i
    global part
    part = 2
    p2 = solve(lines)

    print(p1, p2)


if __name__ == "__main__":
    main()
