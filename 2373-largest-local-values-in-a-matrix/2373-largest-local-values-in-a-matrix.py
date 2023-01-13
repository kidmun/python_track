class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(0, len(grid) - 2):
            row_val = []
            for j in range(0, len(grid) - 2):
                large = 0
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        large = max(grid[row][col], large)
                        
                row_val.append(large)
            ans.append(row_val)
            
        return ans
                        
                    
                
                
        