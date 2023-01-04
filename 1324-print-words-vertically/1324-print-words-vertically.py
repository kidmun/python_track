class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        
        con = []
        for w in s:
            con.append(len(w))
        ans = []   
        larg = max(con)
        for i in range(larg):
            res = ""
            for j in range(len(s)):
                if i < len(s[j]):
                    res += s[j][i]
                else:
                    res += " "
            ans.append(res.rstrip())
            
        return ans
                    
                    
            
        
        