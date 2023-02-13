class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total = sum(nums)
        cur = 0
        n = len(nums)
        if n == 1:
            return 0 
        ans = abs(nums[0] - (total - nums[0]) // (n - 1))
        res = 0
        for i, num in enumerate(nums):
            cur += num
            total -= num
            val1 = cur // (i + 1)
            if (n - i - 1)  > 0:
                val2 = total // (n - i - 1)
            else:
                val2 = 0
            if abs(val1 - val2) < ans:          
                ans = abs(val1 - val2)
                res = i
            
        return res
            
            
            
        