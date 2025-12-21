# Minimum number of ways to multiply
def matrix_multiplication(dimensions):
    if not dimensions or len(dimensions) < 2:
        return 0

    ###### Important: number of matrices is dimensions -1, so deal with four objects only
    n = len(dimensions) - 1  # number of matrices
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            dp[i][j] = float('inf')  # Initialize to infinity
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + dimensions[i] * dimensions[k+1] * dimensions[j+1]
                dp[i][j] = min(dp[i][j], cost)

    return dp

if __name__ == "__main__":
    print(matrix_multiplication([2,3,6,4,5]))
