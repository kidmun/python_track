from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rev = []
        for i in range(len(grid)):
            cols = []
            for j in range(len(grid)):
                cols.append(grid[j][i])
            rev.append(str(cols))
        ans = []
        
        c = Counter(rev)
      
        for g in grid:
            if str(g) in c:
                k = c[str(g)]
                while k > 0:
                    
                    ans.append(g)
                    k -= 1
      
        return len(ans)
        
                
                