def longest_common_subsequence(s1, s2):
    if not s1 or not s2:
        return 0

    #base
    dp = [[0] * (len(s1)) for _ in range(len(s2))]

    # Nivedhan Comment
    # if two characters matches, then 1 + subproblem which i-1, j-1
    # Otherwise max(without i with j, with i without j)
    for i in range(len(s2)):
        for j in range(len(s1)):
            if s2[i] == s1[j]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[len(s2)-1][len(s1)-1]

if __name__ == "__main__":
    s1 = "abc"
    s2 = "abcdefgh"
    print(longest_common_subsequence(s1, s2))