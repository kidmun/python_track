class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = [0]
        pref.extend(list(accumulate(nums)))
        ans = 0
        for i in range(len(nums)):
            val1 = bisect_right(pref, goal + pref[i])
            val2 = bisect_left(pref, goal + pref[i])
            ans += (val1 - max(val2, i+1)) 
        return ans