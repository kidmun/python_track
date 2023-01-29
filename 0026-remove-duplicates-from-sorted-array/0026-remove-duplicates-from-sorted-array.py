class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        prev = nums[0]
        left = 0
        right = 1
    
        while right < len(nums):
            
            if nums[right] > prev:
                nums[left] = prev
                prev = nums[right]
                left += 1
            if right == (len(nums) - 1):
                
                nums[left] = nums[right]
                left += 1
            right += 1
        count = 0
        if len(nums) > 1:
            while left < len(nums):
                nums[left] = "_"
                count += 1
                left += 1
        
        return len(nums) - count
  
                
                
            
            
        