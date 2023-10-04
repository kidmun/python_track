class Solution:
    def minimumObstacles(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        ans = [[float("inf")] * m for _ in range(n)]

        heap = [(0, 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[0] * m for _ in range(n)]
        def inbound(row, col):
            return 0<=row < n and 0 <= col < m
        while heap:
            w, a, b = heappop(heap)
            if heights[a][b]:
                w += 1
            if (a, b) == (n -1, m -1):
                return w
            visited[a][b] = 1
            for x, y in directions:
                row, col = x + a, y + b
                if inbound(row,col) and not visited[row][col]:
                    if w < ans[row][col]:
                        ans[row][col] = w
                        heappush(heap, (w, row, col))