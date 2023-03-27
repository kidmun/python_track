class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] != (i + 1) and nums[nums[i] - 1] != nums[i]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
            
            elif nums[i] != (i + 1) and nums[nums[i] - 1] == nums[i]:
                return nums[i]
            else:
                i += 1