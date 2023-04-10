class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, -1), (0, 1), (1, 0),(-1, 0)]
        if color == image[sr][sc]:
            return image
        n = len(image[0])
        m = len(image)
        val = image[sr][sc]
        def inbound(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or image[row][col] != val:
                return False
            return True
        def dfs(row, col, visited):
            if not inbound(row, col) or (row, col) in visited:
                return
            visited.add((row, col))
            image[row][col] = color 
            for d in directions:
                dfs(row + d[0], col + d[1],visited)
        dfs(sr, sc, set([]))
        return image