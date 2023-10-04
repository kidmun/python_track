class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        for i in range(len(costs)):
            costs[i]  = (abs(costs[i][0] - costs[i][1]), costs[i][0],costs[i][1])
        costs.sort()
        l = 0
        r = 0

        i = n - 1
        ans = 0
        # print(costs)
        while i > -1:
            if l == n // 2:
                while i >= 0:
                    ans += costs[i][2]
                    i -= 1
            elif r == n // 2:
                while i >= 0:
                    ans += costs[i][1]
                    i -= 1
            else:
                # print(l, r, costs[i], ans)
                if costs[i][1] <=  costs[i][2]:
                    ans += costs[i][1]
                    l += 1
                else:
                    ans += costs[i][2]
                    r += 1
                i -= 1
        return ans