class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracking(start, nums, track):
            res.append(track[::])
            for i in range(start, len(nums)):     
                if i > start and nums[i] == nums[i-1]:
                    continue
                backtracking(i+1, nums, track[::] + [nums[i]])
        
        res = []
        nums.sort()
        backtracking(0, nums, [])
        return res
   
        
        
        
            
        