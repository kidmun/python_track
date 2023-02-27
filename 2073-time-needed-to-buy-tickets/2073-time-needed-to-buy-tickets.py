class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i in range(k):
            ans += min(tickets[k], tickets[i])
        for i in range(k + 1, len(tickets)):  
            ans += min(tickets[k] - 1, tickets[i])
        return ans + tickets[k]
            
            
           
        