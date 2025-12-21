def regex_matching(text, pattern):
    # if not text:
    #     if not pattern:
    #         return True
    #     return False

    dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]

    #base case
    dp[0][0] = True
    for i in range(1, len(pattern)+1):
        if pattern[i-1] == '*':
            dp[0][i] = dp[0][i-2]

    for i in range(1, len(text) + 1):
        for j in range(1, len(pattern)+1):
            if text[i-1] == pattern[j-1] or pattern[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            elif pattern[j-1] == '*':
                dp[i][j] = dp[i][j-2]
                if text[i-1] == pattern[j-2] or pattern[j-2] == '.':
                    dp[i][j] = dp[i][j] or dp[i-1][j]
            else:
                dp[i][j] = False

    return dp[len(text)][len(pattern)]


if __name__ == "__main__":
    text = ""
    pattern = "a*b*c*"
    print(regex_matching(text, pattern))
