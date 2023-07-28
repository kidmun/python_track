class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0] * n for _ in range(n)] for _ in  range(k + 1)]
        dp[0][row][column] = 1
        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                      (2, 1), (2, -1), (-2, 1), (-2, -1)]
        for m in range(1, k + 1):
            for r in range(n):
                for c in range(n):
                    for x, y in directions:
                        a, b = x + r, y + c
                        if 0 <= a < n and 0 <= b < n:
                            dp[m][r][c] += dp[m - 1][a][b]
                    dp[m][r][c] /= 8
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += dp[k][i][j]
        return ans