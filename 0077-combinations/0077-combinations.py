class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtracking(n, k, start, track):
            
            if len(track) == k:
                res.append(track[::])
              
                return
            for i in range(start, n + 1):
                track.append(i)
                backtracking(n, k, i + 1, track)
                track.pop()
            
        res = []
        track = []
        backtracking(n, k, 1, track)
  
        return res

            
            
            
            

    
        
      