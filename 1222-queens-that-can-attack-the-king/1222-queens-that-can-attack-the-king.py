class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        ans = []
        goto = [-1, 0, 1]
        for i in goto:
            for j in goto:
                if i == j == 0:
                    continue
                x = king[0]
                y = king[1]
                x += i
                y += j
                while x < 8 and x >= 0 and y >=0 and y < 8:
                    if [x, y] in queens:
                        ans.append([x, y])
                        x += i
                        y += j
                        break
                    x += i
                    y += j
                            
   
        return ans 
  
                
        