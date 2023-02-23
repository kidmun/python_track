class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        count = Counter()
        for trip in trips:
            count[trip[1]] += trip[0]
            count[trip[2]] -= trip[0]
        cur = 0
       
        for p in sorted(count):
            cur += count[p]
            if cur > capacity:
                return False
        return True
                
        



        
        