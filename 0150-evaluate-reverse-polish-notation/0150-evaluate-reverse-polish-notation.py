class Solution:
     
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.isdigit() or len(token) > 1:
                stack.append(token)
            else:
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(str(int(eval(val2 + token + val1))))
        return int(stack[0])

            
        
        