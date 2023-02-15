class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        count = Counter()
        left = 0
        n = len(cards)
        ans = n + 1
        for i, num in enumerate(cards):
            count[num] += 1
            if count[num] > 1:
            
                while cards[left] != num and left < i: 
                    count[cards[left]] -= 1
                    left += 1
                ans = min(ans, i - left + 1)
                
                count[cards[left]] -= 1
                left += 1    
        if ans > n:
            return -1
        else:
            return ans
                    