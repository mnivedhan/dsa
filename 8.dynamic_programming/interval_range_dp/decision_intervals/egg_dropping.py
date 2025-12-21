def egg_dropping(eggs, floors):
    if not eggs or not floors:
        return 0

    num_eggs = eggs + 1
    num_floors = floors + 1
    dp = [[floor if egg == 1 else 0 for floor in range(num_floors)] for egg in range(num_eggs)]

    for egg in range(2, num_eggs):
        for floor in range(1, num_floors):
            dp[egg][floor] = min((1 + max(dp[egg-1][temp_floor-1], dp[egg][floor-temp_floor])) for temp_floor in range (1, floor+1))

    return dp[eggs][floors]

if __name__ == "__main__":
    print(egg_dropping(2,6))