class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def visited(track, k):
            return (track & (1<<k)) != 0
        def off(track,k):
            return track & ~(1<<k)
        def on(track, k):
            return track | (1<<k)
        def backtrack(track, path):
            if int.bit_count(track) == len(nums):
                res.append(path[::])
                return
            for i in range(len(nums)):
                if visited(track, i): 
                    continue
                path.append(nums[i])
                track = on(track, i)
                backtrack(track, path)
                path.pop()
                track = off(track, i)
        res = []
        backtrack(0,[])
        return res