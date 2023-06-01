class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = Counter()
        for num in arr:  
            dp[num] = max(dp[num], (1 + dp[num - difference]))
        return max(dp.values())