class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = 0
        count = 0 
        while i < (n - count):
          
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                count += 1
            else:
                i += 1
        
                