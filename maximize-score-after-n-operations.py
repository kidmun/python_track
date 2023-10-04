class Solution:
    def maxScore(self, nums: List[int]) -> int:
        memo = {}    
        def dp(arr):
            n = len(arr)
            xx = tuple(arr)
            if xx in memo:
                return memo[xx]
            ans = 0
            for i in range(n):
                for j in range(i + 1, n):
                    ans = max(ans,n // 2 *  gcd(arr[i], arr[j]) + dp(arr[:i] + arr[i+1:j]+arr[j +1:]))
            
            memo[xx] = ans
            return ans
        return dp(nums)