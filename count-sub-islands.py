class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
   
        directions = [(1, 0), (-1, 0),(0, 1), (0, -1)]
        m = len(grid1) 
        n = len(grid1[0]) 
        def inbound(row, col):
            nonlocal m, n
            if 0 <= row < m and 0 <= col < n and grid2[row][col] == 1 and (row, col) not in visited:
                return True
            return False
        def dfs(row, col):
            if not inbound(row, col):
                return True
            visited.add((row, col))
            val = grid1[row][col] == 1
            for d in directions:
                val = dfs(row + d[0], col + d[1]) and val
            return val
        visited = set([])
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] and (i, j) not in visited:
                    val = dfs(i, j)
                    if val:
                        ans += 1
        return ans