class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        count = {}
        
        for trip in trips:
        
            if trip[1] in count:
                count[trip[1]] += trip[0]
            else:
                count[trip[1]] = trip[0]
            if trip[2] in count:
                count[trip[2]] -= trip[0]
            else:
                count[trip[2]] = -trip[0]
        cur = 0
       
        for p in sorted(count):
            cur += count[p]
     
            if cur > capacity:
                return False
        return True
                
        



        
        