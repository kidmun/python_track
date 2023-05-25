class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        nums.sort()
        l = 0
        r = len(nums) - 4
        ans = float("inf")
        while r < len(nums):
            ans = min(ans, nums[r] - nums[l])
            l += 1
            r += 1
        return ans