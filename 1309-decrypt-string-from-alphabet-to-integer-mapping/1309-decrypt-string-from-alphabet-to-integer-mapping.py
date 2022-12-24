class Solution:
    def freqAlphabets(self, s: str) -> str:
        li = ['-', 'a', 'b', 'c', 'd', 'e', 'f','g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
     
        
        def convert_digit(digit):
            return li[digit]
        def convert_digit_back(char):
            if char == "0":
                return "0"
            return str(li.index(char))
        ans = []
        for c in s:
            
            if c == '#':
                
                sym1 = convert_digit_back(ans.pop())
                sym2 = convert_digit_back(ans.pop())
                s = sym2 + sym1
                conv = convert_digit(int(s))
              
                ans.append(conv)
            elif c == "0":
                ans.append(c)
                          
            else:
                sym = convert_digit(int(c))
                
                ans.append(sym)
        res = ""
        for a in ans:
            res += a
            
        return res
       
        