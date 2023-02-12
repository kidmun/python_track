class Solution:
    def bestClosingTime(self, customers: str) -> int:
        count = Counter(customers)
        N = 0
        ans = 0
        penality = count["Y"]
        for i, c in enumerate(customers):
            val = N + count["Y"]
           
            if val < penality:
                penality = val
                ans = i
            if c == "Y":
                count["Y"] -= 1
            else:
                N += 1         
        val =  N + count["Y"]
        if val < penality:
                penality = val
                ans = len(customers)
   
        return ans
            
            
            

        
       