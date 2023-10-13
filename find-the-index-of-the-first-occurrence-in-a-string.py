class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(needle), len(haystack)
        # if n < m:
        #     return -1
        # po = 0
        # hashed = 0
        # for i in range(m - 1, -1, -1):
        #     hashed += (ord(needle[i]) - 97 + 1)* (26 ** po) 
        #     hashed %= (10 **9 + 7)
        #     po += 1
        # cur = 0
        # po = 0
        # def checker(s):
        #     if len(s) != m:
        #         return False
        #     for i in range(m):
        #         if s[i] != needle[i]:
        #             return False
        #     return True
        # for i in range(m - 1, -1, -1):
        #     cur += (ord(haystack[i]) - 97 + 1)* (26 ** po)
        #     cur %= (10 **9 + 7)
        #     po += 1
        # if cur == hashed:
        #     return 0
        # for i in range(1, n -m+ 1):
        #     cur -= (ord(haystack[i - 1]) - 97 + 1) * (26 ** (m - 1))
        #     cur *= 26
        #     cur += (ord(haystack[i + m - 1]) - 97 + 1)
        #     cur %= (10 **9 + 7)
        #     if cur == hashed and checker(haystack[i:i + m]):
        #         return i
        # return -1

        #kmp
        prevLsp, i= 0, 1
        
        lsp = [0] * m
        while i < m:
       
            if needle[i] == needle[prevLsp]:
                lsp[i] = prevLsp + 1
                prevLsp += 1
                i += 1
        
            else:
                if prevLsp == 0:
                    lsp[i] = 0
                    i += 1
                else:
                    prevLsp = lsp[prevLsp - 1]
        i, j = 0, 0
     
        while i < n:
         
            if needle[j] == haystack[i]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lsp[j - 1]
            if j == m:
                return i - m
                
        return -1