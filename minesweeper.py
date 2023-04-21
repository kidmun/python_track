class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m = len(board)
        n = len(board[0])
        
        directions=[(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        def inbound(row, col):
            nonlocal m, n
            return 0 <= row < m and 0 <= col < n
        def dfs(row, col):
            count = 0
            for d in directions:
                r = row + d[0]
                c = col + d[1]
                if inbound(r, c) and board[r][c] == "M":
                    count += 1
            if count < 1:
                board[row][col] = "B"
                for d in directions:
                    r = row + d[0]
                    c = col + d[1]
                    if inbound(r, c) and board[r][c] == "E":
                        dfs(r, c)
            else:
                board[row][col] = str(count)
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
        else:
            dfs(click[0], click[1])
        return board