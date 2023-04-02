class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            cur = nums[i]
            ind = i
            while ind < len(nums):
                cur = gcd(cur, nums[ind])
                if cur == 1:
                    if k == 1:
                        ans += (len(nums) - ind)
                    break
                if cur == k:
                    ans += 1
                ind += 1
        return ans