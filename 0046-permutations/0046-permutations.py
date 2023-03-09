class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(track, nums, arr):
           
            if len(track) == len(arr):
                res.append(track[::])
                return
            for i in range(len(nums)):
                track.append(nums[i])
                backtrack(track, nums[:i] + nums[i+1:], arr)
                track.pop()
        res = []
        backtrack([], nums, nums)
        return res
        



                    
                    
        