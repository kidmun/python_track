class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        memo = {}
       
        n = len(stones)
        dp = [0] * n
       
        def dp(res, pos):
            
            if pos == n:
                return res if res >= 0 else float("inf")
            if (res, pos) in memo:
                return memo[(res, pos)]
            val = float("inf")
            val = min(dp(res + stones[pos], pos  +1),dp(res - stones[pos], pos  +1))
   
            memo[(res, pos)] = val
            return memo[(res, pos)]
        return dp(0, 0)