class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            count = Counter()
            for j in range(9):
                if board[i][j] != ".":
                    count[board[i][j]] += 1
            if len(count) > 0 and max(count.values()) > 1:
                # print(i, count,"here")
                return False
        for j in range(9):
            count = Counter()
            for i in range(9):
                if board[i][j] != ".":
                    count[board[i][j]] += 1
            if len(count) > 0 and max(count.values()) > 1:
                # print(i, count)
                return False
        def validate(row, col):
            count = Counter()
            for i in range(row, row + 3):

                for j in range(col, col + 3):
                    if board[i][j] != ".":
                        count[board[i][j]] += 1
            if len(count) > 0 and max(count.values()) > 1:
                # print(i, count)
                return False
            return True
        li = [0, 3, 6]
        for i in li:
            for j in li:
                if not validate(i, j):
                    return False
        return True
        