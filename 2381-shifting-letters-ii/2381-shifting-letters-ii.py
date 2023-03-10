class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        count = Counter()
        for shift in shifts:
            if shift[2] == 0:
                count[shift[0]] -= 1
                count[shift[1]+1] += 1
            else:
                count[shift[0]] += 1
                count[shift[1]+1] -= 1
       
        cur = 0
        ans = [] 
        for i in range(len(s)):
            if i in count:
                cur += count[i]
            if cur < 0:
                val = cur % -26
            else:
                val = cur % 26
            if (ord(s[i]) + val) < 97:
           
                ans.append(chr(97 + 26 - (97 -(ord(s[i]) + val))))
            elif (ord(s[i]) + val) > 122:
                
                ans.append(chr(122 - (26 - ((ord(s[i]) + val) - 122))))
            else:
                ans.append(chr(ord(s[i]) + val))
     
        return "".join(ans)
                
                
            
        