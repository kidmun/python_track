class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured == 0:
            return 0.00000
        dp = [[0 for _ in range(j + 1)] for j in range(100)]
        dp[0][0] = poured
        for i in range(0, 100):
            for j in range(i + 1):
                if i < 99 and dp[i][j] > 1:
                    dp[i + 1][j] += (dp[i][j] - 1) / 2
                    dp[i + 1][ j + 1] += (dp[i][j] - 1) / 2
        if float(dp[query_row][query_glass]) > 1:
          return 1
        return float(dp[query_row][query_glass])