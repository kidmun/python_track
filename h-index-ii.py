class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        n = len(citations)
        right = n
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            val = bisect_right(citations, mid - 1)
            if (n - val) >= mid:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
          
        return ans