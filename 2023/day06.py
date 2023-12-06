import math


def part1(time, distance):
    ans = 1
    for n in range(len(time)):
        t = time[n]
        dist = distance[n]
        wins = 0
        for i in range(0, t):
            travel = (t - i) * i
            if travel > dist:
                wins += 1
        ans *= wins
    return ans


def part2(time, distance):
    sol1 = (-1 * time + math.sqrt(time**2 - 4 * distance)) / 2
    sol2 = (-1 * time - math.sqrt(time**2 - 4 * distance)) / 2
    return abs(int(sol1) - int(sol2))


def main():
    day = "06"
    input = open("2023/inputs/day" + day + ".txt").read().strip().splitlines()
    time = [int(x) for x in input[0].split()[1:]]
    distance = [int(x) for x in input[1].split()[1:]]

    time_p2 = int("".join([str(x) for x in time]))
    distance_p2 = int("".join([str(x) for x in distance]))

    print(part1(time, distance), part2(time_p2, distance_p2))


if __name__ == "__main__":
    main()
