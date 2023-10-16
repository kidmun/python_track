class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        parent = {}
        rank = {}
        for i in range(n):
            for j in range(n):
                parent[(i, j)] = (i, j)
                rank[(i, j)] = 1
        def find(x, y):
            if parent[(x, y)] != (x, y):
                parent[(x, y)] = find(parent[(x, y)][0], parent[(x, y)][1])
            return parent[(x, y)]

        def union(a, b, c, d):
            par_ab = find(a, b) 
            par_cd = find(c, d)
            if par_ab != par_cd:
                if rank[par_ab] >= rank[par_cd]:
                    rank[par_ab] += rank[par_cd]
                    parent[par_cd] = parent[par_ab]
                else:
                    rank[par_cd] += rank[par_ab]
                    parent[par_ab] = parent[par_cd]

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()
        def dfs(row, col):
          
            for a, b in directions:
                x, y = a+ row, b + col
                if inbound(x, y) and (x, y) not in visited:
                    visited.add((x, y))
                    union(x, y, row, col)
                    dfs(x, y)

        for i in range(n):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == 1:
                    visited.add((i, j))
                    dfs(i, j)
        ans = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    ss = set()
                    for a, b in directions:
                        x, y = a + i, b + j
                        if inbound(x, y):
                            ss.add(find(x, y))
                    count = 0
                    for el in list(ss):
                        count += rank[el]    
                    ans = max(ans, count + 1)
        return max(max(rank.values()), ans)