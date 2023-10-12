class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cur = nums[0]
        for i in range(1, n):
            cur &= nums[i]
        x = 2 ** 31 - 1
        count = 0
        ind = 0
        total = 0
        while ind < n:
            x &= nums[ind]
            if  total + x <= cur:
                count += 1
                total += x
                x = 2 ** 31 - 1
            ind += 1
        return count