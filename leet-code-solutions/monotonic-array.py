class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return True
        inc = False
        dec = False
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                if dec:
                    return False
                inc = True
            if nums[i] < nums[i - 1]:
                if inc:
                    return False
                dec = True
        return True
        