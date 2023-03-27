class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        nums.append(-1)
        while i < (len(nums) - 1):
            while nums[i] != i and nums[i] != -1:
                ind = nums[i]
                nums[ind], nums[i] = nums[i], nums[ind]
            i += 1
        for i, num in enumerate(nums):
            if i != num:
                return i
        return (len(nums) - 1)