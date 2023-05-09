class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(maze), len(maze[0])
        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] == "."

        d = deque([(entrance[0], entrance[1])])
        visited = set([(entrance[0], entrance[1])])
        count = 0
        entrance = (entrance[0], entrance[1])
        while d:
            length = len(d)
            for _ in range(length):
                cur = d.popleft()
                if (cur != entrance) and (cur[0] == 0 or cur[0] == m - 1 or cur[1] == 0 or cur[1] == n -1):
                    return count
                for r, c in directions:
                    row = r + cur[0]
                    col = c + cur[1]
                    if inbound(row, col) and (row, col) not in visited:
                        d.append((row, col))
                        visited.add((row, col))
            count += 1
        return -1