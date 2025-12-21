def subset_sum(arr, target):
    if not arr:
        if not target == 0:
            return False
        else:
            return True

    dp = [[False] * (target+1) for _ in range(len(arr))]

    for i in range(len(arr)):
        dp[i][0] = True

    for i in range(len(arr)):
        for j in range(1, target+1):
            # Should I include i or not include i
            if j >= arr[i]:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[len(arr)-1][target]

if __name__ == "__main__":
    input = [3,4,5]
    print(subset_sum(input, 9))

