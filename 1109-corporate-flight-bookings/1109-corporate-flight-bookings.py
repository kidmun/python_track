class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        count = {}
       
        ans = []
        for book in bookings:
            if book[0] in count:
                count[book[0]] += book[2]
            else:
                count[book[0]] = book[2]
            if book[1] + 1 in count:
                count[book[1] + 1] -= book[2]
            else:
                count[book[1] + 1] = -book[2]
        
        prev = 0
        for i in range(1, n + 1):
            if i in count:
                prev += count[i]
            ans.append(prev)
            
        return ans
            
            
                
        