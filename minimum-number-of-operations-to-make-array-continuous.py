class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums) 
        nums = sorted(set(nums))
        ans = n
        for i in range(len(nums)):
            ans = min(ans, n -(bisect_right(nums, nums[i] + n - 1) - i))
        return ans