class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()
        memo = {}
        def dp(ind, mul):
            if ind == n - 1:
                return max(0, mul * satisfaction[ind])
            if (ind, mul) in memo:
                return memo[(ind,mul)]
            memo[(ind, mul)] = max(dp(ind + 1,mul + 1) + mul * satisfaction[ind] ,dp(ind + 1,mul))
            return memo[(ind, mul)]
        return dp(0, 1)