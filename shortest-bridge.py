class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        def inbound(row, col, ):
            return 0 <= row < m and 0 <= col < n 
        def bfs(queue):
            while queue:
                length = len(queue)
                for _ in range(length):
                    cur = queue.popleft()
                    island1.append(cur)
                    for r, c in directions:
                        row = r + cur[0]
                        col = c + cur[1]
                        if (row, col) not in visited and inbound(row, col) and grid[row][col] == 1:
                            queue.append((row, col))
                            visited.add((row, col))
                            
        island1 = deque([])
        visited = set([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] ==  1:
                    bfs(deque([(i, j)]))
                    visited.add((i, j))
                    break
            if len(visited) > 0:
                break
        count = 0
        while island1:
            length = len(island1)
            for _ in range(length):
                cur = island1.popleft()
                for r, c in directions:
                    row = r + cur[0]
                    col = c + cur[1]
                    if (row, col) not in visited and inbound(row, col) and grid[row][col] == 1:
                        return count
                    if  (row, col) not in visited and inbound(row, col) and grid[row][col] == 0:
                        island1.append((row, col))
                        visited.add((row, col))
            count += 1
                        
        return count