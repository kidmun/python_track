class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        n = len(mat)
        m = len(mat[0])
        
        if n * m == r * c:
            ans = []
            count = 0
            for i in range(r):
                
                row = []
                for j in range(c):
                    row.append(mat[count // m][count%m])
                    count += 1
                    
                    
                ans.append(row)
                
            return ans
        
        else:
            return mat
        