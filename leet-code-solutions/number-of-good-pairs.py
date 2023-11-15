class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for key in count:
            x = count[key]
            ans += x * (x - 1) // 2
        return ans
        