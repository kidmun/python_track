class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        if n == 1 or p ==0:
            return 0
        nums.sort()
        low = float("inf")
        high = 0
        for i in range(n - 1):
            low = min(nums[i + 1] - nums[i], low)
            high = max(nums[i + 1] - nums[i], high)
        while low <= high:
            mid = (low + high) // 2
            count = 0
            i = 0
            while i < n - 1:
                if nums[i + 1] - nums[i] <= mid:
                    count += 1
                    i += 1
                i += 1
            if count >= p:
                high = mid - 1
            else:
                low = mid + 1
        return low