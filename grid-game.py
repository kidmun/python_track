class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid[0])
        ind = None
        total1 = sum(grid[0])
        prev1 = 0
        prev2 = 0
        for i in range(n -1):
            prev1 += grid[0][i]
            val1 = max(total1 - prev1, prev2)
            val2 = max(prev2+grid[1][i],total1 - (prev1 + grid[0][i+1]))
        
            if val2 > val1:
                ind = i
                break
            prev2 += grid[1][i]  
        if ind != None:
            return max(prev2, total1 -prev1)
    
        return prev2