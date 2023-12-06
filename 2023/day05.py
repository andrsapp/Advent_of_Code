def getmap(num, alm_map):
    almanac = [x.split() for x in alm_map[1:]]
    for alm in almanac:
        if num in range(int(alm[1]), int(alm[1]) + int(alm[2]) + 1):
            return num - int(alm[1]) + int(alm[0])
    return num


def get_revmap(num, alm_map):
    almanac = [x.split() for x in alm_map[1:]]
    for alm in almanac:
        if num in range(int(alm[0]), int(alm[0]) + int(alm[2]) + 1):
            return num - int(alm[0]) + int(alm[1])
    return num


def checkseed(seed, seeds):
    seed_list = seeds[0].split()[1:]
    for i in range(0, len(seed_list) - 1, 2):
        # if seed in range(int(seed_list[i]), int(seed_list[i])+int(seed_list[i+1])+1):
        if seed >= int(seed_list[i]) and seed <= int(seed_list[i]) + int(seed_list[i + 1]) + 1:
            return True
    return False


def main():
    day = "05"
    input = open("2023/inputs/day" + day + ".txt").read().strip()
    lines = input.split("\n\n")
    seeds = [line.split("\n") for line in lines][0]
    alm_maps = [line.split("\n") for line in lines][1:]

    location_list = []
    for seed in seeds[0].split()[1:]:
        seed = int(seed)
        for i in range(7):
            seed = getmap(seed, alm_maps[i])
        location_list.append(seed)
    print(min(location_list))

    # This took 41 minutes. Need to refactor
    # A bad solution is still a solution though
    # alm_maps.reverse()
    # ans = -1
    # for i in range(min(location_list)):
    #     seed = i
    #     for j in range(7):
    #         seed = get_revmap(seed, alm_maps[j])
    #     if (checkseed(seed, seeds) == True):
    #         ans = i
    #         break
    # ans


if __name__ == "__main__":
    main()
