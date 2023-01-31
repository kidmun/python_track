class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        p1  = 0
        p2 = 0
        n = len(nums1)
        m = len(nums2)
        score1 = 0
        score2 = 0
        res = 0
        while p1 < n and p2 < m:
            if nums1[p1] == nums2[p2]:
                score1 += nums1[p1]
                score2 += nums2[p2]
                val = max(score1, score2)
                res += val
                score1 = 0
                score2 = 0
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                score1 += nums1[p1]
                p1 += 1
                
            else:
                score2 += nums2[p2]
                p2 += 1
            
        if p1 >= n and p2 >= m:
            res += max(score1, score2)
        elif p1 >= n:
            while p2 < m:
                score2 += nums2[p2]
                p2 += 1
        else:
            while p1 < n:
                score1 += nums1[p1]
                p1 += 1
        res += max(score1, score2)
        return res % (10**9 + 7)
        
            
            
                
            
        