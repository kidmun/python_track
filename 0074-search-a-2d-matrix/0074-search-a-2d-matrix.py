class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix) -1 , -1, -1):
            if target >= matrix[i][0]:
                for num in matrix[i]:
                    if num == target:
                        return True
                    
        
        return False
         
        