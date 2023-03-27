class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        ans = []
        while i < n:
            if nums[i] != (i + 1) and nums[nums[i] - 1] != nums[i]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
            
            elif nums[i] != (i + 1) and nums[nums[i] - 1] == nums[i]:
                ans = nums[i]
                i += 1
            else:
                i += 1
        for i in range(len(nums)):
            if i + 1 != nums[i] and i + 1 != ans:
                return [ans,i + 1]