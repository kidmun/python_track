class Solution:
    def longestPrefix(self, s: str) -> str:
        prevLsp, i= 0, 1
        m = len(s)
        
        lsp = [0] * m
        while i < m:
       
            if s[i] == s[prevLsp]:
                lsp[i] = prevLsp + 1
                prevLsp += 1
                i += 1
        
            else:
                if prevLsp == 0:
                    lsp[i] = 0
                    i += 1
                else:
                    prevLsp = lsp[prevLsp - 1]
        # print(lsp)
        return s[:lsp[-1]]