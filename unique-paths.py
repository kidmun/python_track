class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        grid[m - 1][n - 1] = 1
        for col in range(n- 1, -1, -1):
            for row in range(m -1, -1, -1):
                if row == m - 1 and col == n - 1:
                    continue
                grid[row][col] = grid[row + 1][col] + grid[row][col + 1]
        return grid[0][0]