def job_scheduling(startTime, endTime, profit):

    dp = profit[:]

    for i in range(1, len(profit)):
        for j in range(i):
            if endTime[j] <= startTime[i]:
                dp[i] = max(dp[i], dp[j] + profit[i])


    return max(dp)

if __name__ == "__main__":
    startTime = [1,2,3,4,6]
    endTime = [3,5,10,6,9]
    profit = [20,20,100,70,60]

    # Transpose the matrix rows to columns
    combined = zip(startTime, endTime, profit)
    # Sort based on the second element of the tuple (endTime)
    combined_sorted = sorted(combined, key=lambda x: x[1])
    # Transpose it back to rows but returns as tuple
    startTime, endTime, profit = zip(*combined_sorted)

    print(job_scheduling(list(startTime), list(endTime), list(profit)))