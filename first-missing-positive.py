class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_pos = float("inf")
        n = len(nums)
        for num in nums:
            if num >= 0:
                min_pos = min(min_pos, num)

        if min_pos == float("inf") or min_pos > 1:
            return 1
        i = 0
        while i < n:
            if nums[i] > -1 and (nums[i] - min_pos) < n and (nums[i] - min_pos) != i and nums[(nums[i] - min_pos)] != nums[i]:               
                nums[(nums[i] - min_pos)], nums[i] =  nums[i], nums[(nums[i] - min_pos)]
            else:
                i += 1 

        for num in nums: 
            if num != min_pos:
                return min_pos
            min_pos += 1
        return max(nums) + 1