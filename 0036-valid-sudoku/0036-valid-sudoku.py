class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = []        
        cols = []
        sub_boxes = []
        count = 1
        for i in range(9):
            row = []
            col = []
            for j in range(9):
                if board[i][j].isdecimal():
                    row.append(board[i][j])
                if board[j][i].isdecimal():
                    col.append(board[j][i])
                if i == 0 or i == 3 or i == 6:
                    if j == 0 or j == 3 or j ==6:
                        box = []

                        if i < 7 and j < 7:
                            for r in range(i, i + 3):
                                for c in range(j, j + 3):
                                    if board[r][c].isdecimal():
                                        box.append(board[r][c])
                        sub_boxes.append(box)
            rows.append(row)
            cols.append(col)
     
        for r in rows:
            if len(r) != len(set(r)):
                return False
        for c in cols:
            if len(c) != len(set(c)):
                return False
        for box in sub_boxes:
            if len(box) != len(set(box)):
                return False
        return True
        
    
        
                        

                
        