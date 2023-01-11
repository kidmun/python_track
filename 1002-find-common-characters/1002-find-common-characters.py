class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        con = []
        alph = []
        for w in words:
            
            dic = [0] * 26
            asc = ord('a')
            for c in w:
                a = ord(c)
                dic[a - asc] += 1
                
            con.append(dic)
        ans = []
        for i in range(26):
            li = []
            for j in range(len(words)):
                li.append(con[j][i])
            ans.append(min(li))
        res = []
        print(con)
        asc = 97
        print(ans)
        for i, a in enumerate(ans):
            if a > 0:
                x = a
                while x > 0:
                    res.append(chr(asc + i))
                    x -= 1
            
            
                
        return res
        
        