class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        count_row = {}
        count_col = {}
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            
            for j in range(n):
                if matrix[i][j] == 0:
                    if j in count_col:
                        count_col[j] += 1
                    else:
                        count_col[j] = 1
                    if i in count_row:
                        count_row[i] += 1
                    else:
                        count_row[i] = 1
            
        for key, amount in count_row.items():
            if amount >= 1:
                for j in range(n):
                    matrix[key][j] = 0
        for key, amount in count_col.items():
            if amount >= 1:
                for i in range(m):
                    matrix[i][key] = 0
                    
                    
                
                    
                    