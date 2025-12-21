def minimum_jump_to_reach_end(array):
    """DP Solution - O(n²) time, O(n) space"""
    if not array:
        return 0

    dp = [float('inf')] * (len(array))

    # base case
    dp[0] = 0

    for i in range(1, len(array)):
        # Check all previous positions that can reach i
        for j in range(i):
            if array[j] >= (i - j):
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[-1]

if __name__ == "__main__":
    array = [2,3,1,1,2,4,2,0,1,1]
    print(minimum_jump_to_reach_end(array))

