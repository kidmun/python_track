class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        parent = {}
        visited = {}
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                parent[(i, j)] = (i, j)
                visited[(i, j)] = False
        def inbound(r, c):
            return 1 <= r <= row and 1 <= c <= col and visited[(r, c)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            p_x = find(x)
            p_y = find(y)
            # print(p_x, p_y, x, y)
            if (p_x[0]==1 and p_y[0] == row) or (p_x[0]==row and p_y[0] == 1):
                return True
            
            if p_x != p_y:
                if p_x[0] == 1 or p_x[0] == row:
                    parent[p_y] = p_x
                else:
                    parent[p_x] = p_y
            # print(parent[p_x], parent[p_y], "ss")
            return False
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(cells) -1, -1, -1):
            p1, p2 = cells[i][0], cells[i][1]
            visited[(cells[i][0], cells[i][1])] =True
            for a, b in directions:
                x = a + p1
                y = b + p2
                if inbound(x, y):
                    if union((p1, p2), (x, y)):
                        return i
        return 1