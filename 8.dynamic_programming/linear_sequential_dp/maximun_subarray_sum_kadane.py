def maximum_subarray_sum(array):
    max_sum = 0
    if not array:
        return max_sum

    dp = [0] * len(array)
    dp[0] = array[0]

    for i in range(1, len(array)):
        dp[i] = max(array[i], dp[i-1] + array[i])
        if dp[i] > max_sum:
            max_sum = dp[i]

    return max_sum

if __name__ == "__main__":
    array = [2,3,-8,7,-1,2,3]
    print(maximum_subarray_sum(array))



