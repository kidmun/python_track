class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        free1, free2 = 0, 0 
        hold1, hold2 = float("-inf"),float("-inf")
        for i in range(n):
            free2  = max(free2, hold2 + prices[i])
            hold2 =max(hold2, free1 - prices[i])
            free1  =max(free1, hold1 + prices[i])
            hold1 = max(hold1, -prices[i])
        return free2
        