class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        right = len(piles) - 2
        left = 0
        ans = 0
        while left < right:
            ans += piles[right]
            right -= 2
            left += 1
            
            
        return ans