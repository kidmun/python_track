class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        obj = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i - j in obj:
                    if obj[i - j] != matrix[i][j]:
                        return False
                else:
                    obj[i - j] = matrix[i][j]
        return True
        