class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        maximum = 0
        right = len(nums) - 1 
         
        while (right - 2) >= 0:
            if (nums[right-2] + nums[right - 1]) > nums[right]:
                maximum = max(maximum, nums[right - 2] + nums[right - 1] + nums[right]) 
            right -= 1
            
        return maximum
            
                    
        
                