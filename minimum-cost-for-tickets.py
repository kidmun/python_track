class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        ss = days
        def dp(cur):
            if cur > days[-1]:
                return 0
            if cur not in ss:
                return dp(cur + 1)
            if cur in memo:
                return memo[cur]
            val1 = costs[0] + dp(cur + 1)
            val2 = costs[1] + dp(cur + 7)
            val3 = costs[2] + dp(cur + 30)
            memo[cur] = min(val1, val2, val3)
            return memo[cur]
        return dp(1)