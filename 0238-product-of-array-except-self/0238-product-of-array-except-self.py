class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * (n + 2)
        suff = [0] * (n + 2)
        pref[0] = suff[0 ] = 1
        pref[-1] = suff[-1] = 1 
        cur1 = 1
        cur2 = 1
        for i in range(n):
            cur1 *= nums[i]
            cur2 *= nums[n - i - 1]
            pref[i+1] = cur1
            suff[n - i] = cur2
     
        for i in range(1, n+1):
      
            nums[i-1] = pref[i-1] * suff[i+1]
        return nums
        