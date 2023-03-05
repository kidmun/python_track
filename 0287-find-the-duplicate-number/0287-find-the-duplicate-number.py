class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        nums.sort()
        while left <= right:
            mid = (left + right) // 2
       
            if (n - mid) > (n - nums[mid]):
                left = mid + 1
            else:
                right = mid - 1
        return nums[mid]
            
        