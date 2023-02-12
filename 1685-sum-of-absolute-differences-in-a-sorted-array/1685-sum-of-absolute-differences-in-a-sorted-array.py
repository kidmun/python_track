class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        cur = 0
        n = len(nums)
        for i, num in enumerate(nums):
            cur += num
            val1 = (i + 1) * num - cur
            val2 = total - (n - i) * num  
            total -= num
            nums[i] = val1 + val2
        return nums
            
            
        