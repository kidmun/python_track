class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        cur = 0
        for i, num in enumerate(nums):
            total -= num
            if cur == total:
                return i
            cur += num
        return -1
                
        