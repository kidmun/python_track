class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        large = max(nums)
     
        arr = [0] * (large + 1)
        sorted_nums = [] 
        for n in nums:
            arr[n] += 1
       
        for i, a in enumerate(arr):
            x = a
            
            while x > 0:          
                sorted_nums.append(i)
               
                x -= 1
        for i, num in enumerate(nums):
            nums[i] = sorted_nums.index(num)
        return nums
            
        