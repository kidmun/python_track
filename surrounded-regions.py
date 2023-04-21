class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(board)
        n = len(board[0])
        def inbound(row, col):
            return 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == "O"
        def dfs(row, col):
            board[row][col] = "0"
            for d in directions:
                r = row + d[0]
                c = col + d[1]
                if inbound(r, c):
                    dfs(r, c)
        for i in range(n):
            if board[0][i] == "O":
                dfs(0, i)
        for i in range(n):
            if board[m - 1][i] == "O":
                dfs(m - 1, i)
        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
        for i in range(m):
            if board[i][n - 1] == "O":
                dfs(i, n - 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "0":
                    board[i][j] = "O"