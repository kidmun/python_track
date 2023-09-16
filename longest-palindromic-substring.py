class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = [0, 0]
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i+1] = True
                res = [i, i + 1]
       
        for dif in range(2, n):
            for i in range(n - dif):
                if s[i] == s[i + dif] and dp[i + 1][i + dif -1]:
                    dp[i][i+dif] = True
                    res = [i, i + dif]
        return s[res[0]:res[1] + 1]