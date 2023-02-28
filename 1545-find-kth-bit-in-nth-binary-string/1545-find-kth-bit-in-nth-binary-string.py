class Solution:
    def recu(self, n):
        if n == 1:
            return "0"
        val = self.recu(n-1)
        inv = []
        for ch in val:
            if ch == "0":
                inv.append("1")
            else:
                inv.append("0")
        inv.reverse()
        inv = "".join(inv)
        
        
        return val + "1" + inv
    def findKthBit(self, n: int, k: int) -> str:
        val = self.recu(n)
    
        return val[k-1]
        
       
        
        