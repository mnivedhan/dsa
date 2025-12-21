def wildcard_matching(text, pattern):
    if len(text) == 0:
        if len(pattern) == 0:
            return True
        return False

    dp = [[False] * (len(pattern)+1) for _ in range(len(text)+1)]

    # Base case
    dp[0][0] = True

    for i in range(1, len(text) + 1):
        for j in range(1, len(pattern) + 1):
            if text[i-1] ==  pattern[j-1] or pattern[j-1] == '?':
                dp[i][j] = dp[i-1][j-1]
            elif pattern[j-1] == '*':
                dp[i][j] = dp[i-1][j] or dp[i][j-1]
            else:
                dp[i][j] = False

    return dp[len(text)][len(pattern)]


if __name__ == "__main__":
    text = "abbbbbbbbc"
    pattern = "a*c"
    print(wildcard_matching(text, pattern))

