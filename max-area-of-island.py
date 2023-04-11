class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set([])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        def inbound(row, col):
            if -1 < row < m and -1 < col < n and grid[row][col] == 1:
                return True
            return False
        def dfs(row, col):
            nonlocal count, ans
            if not inbound(row, col) or (row, col) in visited:
                ans = max(count, ans)
                return
            count += 1
            visited.add((row, col))
            for d in directions:
                dfs(row + d[0], col+d[1])
        ans = 0
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    count = 0
                    dfs(i, j)
        return ans