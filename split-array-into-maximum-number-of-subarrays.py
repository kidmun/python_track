class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        cur = nums[0]
        for i in range(1, n):
            cur &= nums[i]
        x = None
        count = 0
        ind = 0
       
        total = 0
        while ind < n:
            if x == None:
                x = nums[ind]
            else:
                x &= nums[ind]
            if  total + x <= cur:
                count += 1
                total += x
                x = None
           
            ind += 1
        return count