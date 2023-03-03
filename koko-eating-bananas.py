class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = None
        while left <= right:
            mid = (left + right) // 2
            cur = 0
            for p in piles:
                if p <= mid:
                    cur += 1
                else:
                    cur += ceil((p / mid))
          
            if cur <= h:
                ans = mid
                right = mid - 1 
            else:
                left = mid + 1

        return ans