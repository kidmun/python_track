class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        right = max(nums)
        left = 1
        ans = None
        while left <= right:
            
            mid = (left + right) // 2
            cur = 0
            for num in nums:
                cur += ceil(num/mid)
            if cur <= threshold:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans