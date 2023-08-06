class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold = [0] * n
        hold[0] = -prices[0]
        free = [0] * n
        for i in range(1, n):
            hold[i] = max(hold[i - 1], free[i - 2] - prices[i])
            free[i] = max(free[i - 1], hold[i - 1] + prices[i])

        return free[-1]