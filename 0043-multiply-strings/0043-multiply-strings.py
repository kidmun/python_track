class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        li = []
        for i in range(len(num1) - 1, -1, -1):
            res = ""
            rem = 0
            for j in range(len(num2) - 1, -1, -1):
                n1 = int(num1[i])
                n2 = int(num2[j])
                val = (n1 * n2) + rem
         
                if j == 0:
                    res = str(val) + res
                else:
                    res = str(val % 10) + res
                    rem = val // 10
            for k in range(len(num1) - i - 1):
                res += '0'
            li.append(res)
        large = [len(x) for x in li]
        rem = 0
        answer = ""
       
        index = -1
        for i in range(max(large)):
            res = 0
            
            for l in li:
                if i < len(l):
                    res += int(l[index])
            val = res + rem
            rem = (res + rem) // 10
            if i == (max(large) - 1):
                answer = str(val) + answer
            else:
                answer = str(val % 10) + answer
            index -= 1
        if answer[0] == "0":
            return "0"
        return answer
                
            
                    
                    
                    
                
                
                
                
                
            
     