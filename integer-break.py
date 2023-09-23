class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            for j in range(1, n - i + 1):
                dp[i] = max(dp[i], dp[i + j] * j)
     
        return dp[0]
        # ans = 0
        # memo = {}
        # def dp(cur_sum):
        #     nonlocal ans

        #     if cur_sum == n:
        #         return 1
        #     if cur_sum > n:
        #         return 0
        #     if cur_sum in memo:
        #         return memo[cur_sum]
        #     val = 0
        #     for i in range(1, n):
        #         val = max(val, dp(cur_sum + i) * i)
        #     memo[cur_sum] = val
        #     return memo[cur_sum]
        # return dp(0)