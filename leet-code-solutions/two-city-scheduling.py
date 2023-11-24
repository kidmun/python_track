class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs = [(abs(x[0] - x[1]), x[0], x[1]) for x in costs]
        costs.sort()
        l = 0
        r = 0
        ans = 0
        for i in range(n - 1, -1, -1):
            if costs[i][1] <= costs[i][2]:
                l += 1
                ans += costs[i][1]
            else:
                r += 1
                ans += costs[i][2]
            if l == n // 2:
                for j in range(i -1, -1, -1):
                    ans += costs[j][2]
                break
            if r == n  // 2:
                for j in range(i -1, -1, -1):
                    ans += costs[j][1]
                break
        return ans

                

       