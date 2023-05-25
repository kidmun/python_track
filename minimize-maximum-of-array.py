class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        pref = list(accumulate(nums))
        ans = float("-inf")
        for i in range(1, len(nums) + 1):
            ans = max(ans, ceil(pref[i - 1] / i))
        return ans