class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def findMax(nums):
            if len(nums) == 1:
                return nums[0]
            rob1, rob2 = 0, 0
            for num in nums:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(findMax(nums[:len(nums) - 1]),findMax(nums[1:]))