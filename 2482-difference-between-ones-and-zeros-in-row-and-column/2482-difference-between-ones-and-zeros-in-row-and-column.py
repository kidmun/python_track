from collections import Counter
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        r_list = []
        c_list = []
        diff = []
        for g in grid:
            row_count = Counter(g)
            r_list.append(row_count)
           
        for i in range(len(grid[0])):
            li = []
            for j in range(len(grid)):
                li.append(grid[j][i])
            col_count = Counter(li)
            c_list.append(col_count)
   
            
        for i in range(len(grid)):
            if 0 in r_list[i]:
                r_zeros = r_list[i][0]
            else:
                r_zeros = 0
            if 1 in r_list[i]:
                r_ones = r_list[i][1]
            else:
                r_ones = 0
            
            row = []
            for j in range(len(grid[0])):
                
                if 0 in c_list[j]:
                    c_zeros = c_list[j][0]
                else:
                    c_zeros = 0
                if 1 in c_list[j]:
                    c_ones = c_list[j][1]
                else:
                    c_ones = 0
                row.append(r_ones + c_ones - r_zeros - c_zeros)
            diff.append(row)
        return diff
                
                
            
            
        