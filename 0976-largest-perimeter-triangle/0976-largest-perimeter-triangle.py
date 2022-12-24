class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maximum = 0
        right = len(nums) - 1 
        left = right - 2 
        while left >= 0:
            if (nums[left] + nums[left + 1]) > nums[right]:
                maximum = max(maximum, nums[left] + nums[left + 1] + nums[right]) 
            right -= 1
            left = right - 2 
        return maximum
            
                    
        
                