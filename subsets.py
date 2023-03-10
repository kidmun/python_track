class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      
  
        def backtracking(start, nums, track):
            res.append(track[::])
            if len(track) >= n:
                return
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtracking(i, nums[:i]+ nums[i+1:], track)
                track.pop()
        res = []
        n = len(nums)        
        backtracking(0, nums, [])
        return res