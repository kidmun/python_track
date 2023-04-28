class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        queue = deque([(0, 0)])
        visited = set([(0, 0)])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0
        count = 1
        while queue:
            length = len(queue)
            for i in range(length):
                cell = queue.popleft()
                if cell[0] == n -1 and cell[1] == n - 1:
                    return count
                for r, c in directions:
                    row = cell[0] + r
                    col = cell[1] + c
                    if (row, col) not in visited and inbound(row, col):
                        queue.append((row, col))
                        visited.add((row, col))
            count += 1
        return -1