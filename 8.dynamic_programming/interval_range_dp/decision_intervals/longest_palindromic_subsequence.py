def longest_palindromic_sequence(input):
    if not input:
        return 0
    if len(input) == 1:
        return 1

    dp = [[0]* len(input) for _ in range(len(input))]

    # base
    for i in range(len(input)):
        dp[i][i] = 1

    n = len(input)
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if input[i] == input[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]


if __name__ == "__main__":
    input = "bbcabbcd"
    print(longest_palindromic_sequence(input))


