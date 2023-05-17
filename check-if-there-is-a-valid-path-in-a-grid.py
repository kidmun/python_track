class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        parent = {}
        n = (len(grid[0]) * len(grid))
        rank = [1] * n

        for i in range(n):
            parent[i] = i
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x != parent_y:
                if rank[parent_x] >= rank[parent_y]:
                    rank[parent_x] += rank[parent_y]
                    parent[parent_y] = parent[parent_x]
                else:
                    rank[parent_y] += rank[parent_x]
                    parent[parent_x] = parent[parent_y]
        right = {1:{1, 3, 5}, 2:{}, 3:{}, 4:{3, 5, 1}, 5:{}, 6:{1,3,5}}
        down = {1:{},2:{2, 6, 5}, 3:{2,6,5},4:{2,5,6},5:{}, 6:{}}
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if c + 1 < len(grid[0]) and grid[r][c+1] in right[grid[r][c]]:
                    union(r  * len(grid[0]) + c, r  * len(grid[0]) + c + 1)
                if r + 1 < len(grid) and grid[r + 1][c] in down[grid[r][c]]:
                    union(r  * len(grid[0]) + c, (r + 1)  * len(grid[0]) + c)
      
        return find(0) == find(len(grid) * len(grid[0]) - 1)