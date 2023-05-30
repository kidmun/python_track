class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev1 = cost[-1]
        prev2 = 0
        for i in range(len(cost) - 2, -1, -1):
            temp = prev1
            prev1 = min(prev1, prev2) + cost[i]
            prev2 = temp
        return min(prev1, prev2)