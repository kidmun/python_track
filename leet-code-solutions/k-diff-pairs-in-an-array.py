class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        if k == 0:
            count = Counter(nums)
            for key in count:
                if count[key] > 1:
                    ans += 1
        nums = list(set(nums))
        nums.sort()
        n = len(nums)
        for i in range(n):
            ans += bisect_right(nums, nums[i] + k, i + 1) - bisect_left(nums, nums[i] + k, i + 1)
        return ans 
        