class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
   
        back = []
        n  = len(cardPoints)
        total = 0
        forward = []
        for num in cardPoints:
            total += num
           
            forward.append(total)
        total = sum(cardPoints)
        for num in cardPoints:
            back.append(total)
            total -= num
        left = 0
        right = n - 1
        ans = 0
        left_t = 0
        right_t = 0
        while left <= right and k > 0:
            if (forward[left + k - 1] - left_t) >= (back[right - k + 1]-right_t):
                ans += cardPoints[left]
               
                left_t += cardPoints[left]
                left += 1
            else:
                ans += cardPoints[right]
                right_t += cardPoints[right]
                
                right -= 1
            k -= 1
        return ans
                


            