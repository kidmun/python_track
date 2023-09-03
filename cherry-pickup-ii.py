class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(1,-1), (1, 0), (1, 1)]
        ans = 0
        def inbound(row, col):
            nonlocal n, m
            return -1 < row < n and -1< col < m
        memo = {}
        def dfs(cur1, cur2):
        
            if cur1 == cur2:
                return float("-inf")
            xx = (cur1[0],cur1[1],  cur2[0], cur2[1])
            if xx in memo:
                return memo[xx]
            val = 0
            for a, b in directions:
                for c, d in directions:
                    row = a + cur1[0]
                    col = b + cur1[1]
                    x, y = cur2[0] + c, cur2[1] + d
                    if inbound(row, col) and inbound(x, y): 
                        val = max(dfs((row,col), (x, y)), val)
            
            memo[xx] = val + grid[cur1[0]][cur1[1]] + grid[cur2[0]][cur2[1]]
            return memo[xx]
        return dfs((0, 0), (0, m - 1))