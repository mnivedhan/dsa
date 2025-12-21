def cutting_rod(profit_map, length):
    cut_pieces = list(profit_map.keys())

    dp = [[0] * (length + 1) for _ in range(len(cut_pieces))]

    for i in range(len(cut_pieces)):
        for j in range(1, length+1):
            if j >= cut_pieces[i]:
                dp[i][j] = max(dp[i-1][j], profit_map.get(cut_pieces[i]) + dp[i][j-cut_pieces[i]])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[len(cut_pieces)-1][length]

if __name__ == "__main__":
    profit_map = {1: 2, 2: 5, 3: 7, 4: 8}
    length =  5
    print(cutting_rod(profit_map, length))