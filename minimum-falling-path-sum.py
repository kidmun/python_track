class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        dp = [[0] * n for _ in range(n)]
        dp[-1] = matrix[-1]
        for i in range(n - 2, -1, -1):
            for j in range(n):
                if j == 0:
                    dp[i][j] = min(dp[i + 1][j], dp[i + 1][j+ 1]) + matrix[i][j]
                elif j == n - 1:
                    dp[i][j] = min(dp[i + 1][j], dp[i + 1][j - 1]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i + 1][j],dp[i + 1][j + 1],  dp[i + 1][j - 1]) + matrix[i][j]
        return min(dp[0])