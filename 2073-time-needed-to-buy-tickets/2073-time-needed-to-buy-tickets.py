class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i in range(k):
            ans += min(tickets[k], tickets[i])
        val = tickets[k] - 1
        for i in range(k + 1, len(tickets)):
            ans += min(val, tickets[i])
        return ans + tickets[k]
            
            
           
        