class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        ans = nums[0]
        while left <= right:
            mid = (left + right) // 2
            if (nums[mid] < nums[n - 1]):
                ans = min(ans,nums[mid])
                right = mid - 1
            else:
                ans = min(ans,nums[mid])
                left = mid + 1
        return ans

        