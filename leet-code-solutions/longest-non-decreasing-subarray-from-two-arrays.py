class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        dp = [(1, 1)]
        for i in range(1, n):
            val1 = max(dp[i - 1][0] + 1 if nums1[i  - 1] <= nums1[i] else 1, dp[i - 1][1] + 1 if nums2[i  - 1] <= nums1[i] else 1)
            val2 = max(dp[i - 1][0] + 1 if nums1[i  - 1] <= nums2[i] else 1, dp[i - 1][1] + 1 if nums2[i  - 1] <= nums2[i] else 1)
            dp.append((val1, val2))
        ans = 1
        for i in range(n):
            ans = max(ans, dp[i][0], dp[i][1])
        return ans



      
        


            

        