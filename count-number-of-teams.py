class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        dp = [[0, 0] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    dp[i][0] += 1
                else:
                    dp[i][1] += 1
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if rating[j] > rating[i]:
                    ans += dp[j][0]
                else:
                    ans += dp[j][1]
        return ans
    
    
\