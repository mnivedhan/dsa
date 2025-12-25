def min_coin_change(coins, target):
    if not coins or target == 0:
        return 0

    n = len(coins)
    # dp[i][j] = min coins to make amount j using first i coins
    dp = [[float('inf')] * (target + 1) for _ in range(n + 1)]

    # Base case: 0 coins needed to make amount 0
    for i in range(n + 1):
        dp[i][0] = 0

    # Fill the DP table1
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # When the amount is greater than coin, Take the current coin (if possible)
            if j >= coins[i-1]:
                dp[i][j] = min(dp[i-1][j], 1 + dp[i-1][j - coins[i-1]])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][target] if dp[n][target] != float('inf') else -1


if __name__ == "__main__":
    coins = [1,5]
    target = 1
    print(min_coin_change(coins, target))