class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        ans = 0
        count = Counter()
        count[0] = 1
        cur = 0
        for num in nums:
            cur += num
            if (cur - k) in count:
                ans += count[cur - k]
            count[cur] += 1
        return ans
        
        