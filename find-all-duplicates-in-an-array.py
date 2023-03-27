class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] != (i + 1) and nums[nums[i] - 1] != nums[i]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
            else:
                i += 1
        ans = []
        for i in range(1, n + 1):
            if i != nums[i-1]:
                ans.append(nums[i-1])
        return ans