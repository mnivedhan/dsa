def min_coin_change_unbounded(coins, target):
    if not coins or target == 0:
        return 0

    n = len(coins)
    # dp[i][j] = min coins to make amount j using first i coins (unlimited)
    dp = [[float('inf')] * (target + 1) for _ in range(n + 1)]

    # Base case: 0 coins needed to make amount 0
    for i in range(n + 1):
        dp[i][0] = 0

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            # Don't take the current coin
            dp[i][j] = dp[i-1][j]

            # Take the current coin (if possible) - use SAME ROW for unbounded
            if j >= coins[i-1]:
                dp[i][j] = min(dp[i][j], 1 + dp[i][j - coins[i-1]])

    return dp[n][target] if dp[n][target] != float('inf') else -1

if __name__ == "__main__":
    coins = [1,2,5]
    target = 5
    print(min_coin_change_unbounded(coins, target))
