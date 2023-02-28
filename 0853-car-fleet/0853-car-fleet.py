class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i, pos in enumerate(position):
            position[i] = (pos, (target - pos)/speed[i])
        position.sort()  
        count = 1
        prev = position[-1][1]
        for i in range(len(position) - 2, -1, -1):
            if position[i][1] > prev:
                count += 1
                prev = position[i][1] 
        return count
            
        
      
       
        
            
        
        