class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        res = 0
        for r in range(len(grid) - 2):
            for c in range(len(grid[0]) - 2):
                all_sum = []
                x = 0
                diag1 = []
                diag2 = []
                digit_flag = True
                nums = []
                for i in range(r, r + 3):
                    row = []
                    col = []
                   
                    y = 0
                    
                    for j in range(c, c + 3):
                        if grid[i][j] < 1 or grid[i][j] > 9:
                            digit_flag = False
                        nums.append(grid[i][j])
                        row.append(grid[i][j])
                        col.append(grid[r + y][c + x])
                        if x - y == 0:
                            diag1.append(grid[i][j])
                        if x + y == 2:
                            diag2.append(grid[i][j])
                        y += 1
                    x += 1
                    all_sum.append(sum(row))
                    all_sum.append(sum(col))
                all_sum.append(sum(diag1))
                all_sum.append(sum(diag2))
                if len(set(all_sum)) == 1 and digit_flag and len(set(nums)) == 9:
                    res += 1
                        
                        
        return res
        