class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        count = {}
        pos = []
        for trip in trips:
            pos.extend(trip[1:])
            if trip[1] in count:
                count[trip[1]] += trip[0]
            else:
                count[trip[1]] = trip[0]
            if trip[2] in count:
                count[trip[2]] -= trip[0]
            else:
                count[trip[2]] = -trip[0]
        pos = list(set(pos))
        pos.sort()
        cur = 0
       
        for p in pos:
            cur += count[p]
     
            if cur > capacity:
                return False
        return True
                
        



        
        