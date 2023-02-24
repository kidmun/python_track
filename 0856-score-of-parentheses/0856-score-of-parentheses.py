class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        i = 0
        while i < len(s):
            if s[i] == "(":
                if s[i+1] == ")":
                    stack.append("()")
                    i += 1
                else:
                    stack.append("(")
                    
            else:
                count = 0 
           
                while stack and stack.pop() == "()":
                    count += 1
                for _ in range(count * 2):
                    stack.append("()")     
                
            i += 1
   
        return len(stack)
                
                    
                
      

        
        