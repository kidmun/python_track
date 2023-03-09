class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtracking(start, nums, track, arr):
            res.add(tuple(track[::]))
            if len(track) >= len(arr):
                return
            for i in range(start, len(nums)):   
                track.append(nums[i])                
                backtracking(i, nums[:i]+ nums[i+1:], track, arr)
                track.pop()   
        res = set()
        nums.sort()
        backtracking(0, nums, [], nums)
        
        return [list(x) for x in list(res)]
        
        
        
            
        