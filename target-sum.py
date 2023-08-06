class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        def find(i, cur):
            if i == n:
                if cur == target:
                    return 1
                return 0
            if (i, cur) not in memo:
                memo[(i, cur)] = find(i + 1, cur + nums[i]) +  find(i + 1, cur - nums[i])
            return memo[(i, cur)]
        return find(0, 0)