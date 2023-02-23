class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cur = 0
        for i, num in enumerate(nums):
            cur += num
            nums[i] = cur
        return nums
            