class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(1, n):
            for j in range(n - i):
                if s[j] == s[j + i]:
                    dp[j][j + i] = dp[j + 1][j + i  - 1] + 2 
                else: 
                    dp[j][j + i] = max(dp[j + 1][j + i],dp[j][j + i -1])
        return dp[0][n - 1]