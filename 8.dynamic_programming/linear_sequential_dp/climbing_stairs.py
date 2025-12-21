def num_ways_to_climb(stairs):
    if stairs <= 1:
        return 1
    # This is 1D DP problem
    dp = [0 for _ in range(stairs+1)] # Adding +1 as I am also considering 0 th index

    # base case
    dp[0] = 1
    dp[1] = 1

    for i in range(2, stairs+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[stairs]

if __name__ == "__main__":
    print(num_ways_to_climb(5))