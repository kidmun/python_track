class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        def backtracking(start, track, ans):   
            if start > len(nums):
                return
            if len(track) >= 2:
                ans.add(tuple(track[::]))
            for i in range(start, len(nums)):
                flag = False  
                if not track or nums[i] >= track[-1]: 
                    track.append(nums[i])
                    flag = True
                backtracking(i + 1, track, ans)
                if flag:
                    track.pop()
            return ans
        ans = set()
        return list(set(backtracking(0, [], ans)))