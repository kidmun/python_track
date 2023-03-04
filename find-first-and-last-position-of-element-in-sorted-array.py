class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        val1 = -1
        while left <= right:
            mid = (left + right) // 2
     
            if nums[mid] == target:
                val1 = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        left = 0
        right = n - 1
        val2 = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                val2 = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [val2, val1]