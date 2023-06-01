class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[0 for i in range(j + 1)] for j in range(len(triangle))]
        dp[len(triangle) - 1] = triangle[len(triangle) - 1][::]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][ j + 1]) + triangle[i][j]
        return dp[0][0]