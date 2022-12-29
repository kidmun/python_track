class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        
        ans = []
        line_ans= ""
        block_flag = False
    
        for line in source:
            n =len(line)
            i = 0
            while i < n:
                if i < (n - 1) and not block_flag and line[i] == '/' and line[i+1] == "/":
                    i = len(line)
                elif i < (n - 1) and not block_flag and line[i] == '/' and line[i + 1] == "*":
                    block_flag = True
                    i += 1
                elif i < (n - 1) and block_flag and line[i] == "*" and line[i + 1] == "/":
                    block_flag = False
                    i += 1
                elif not block_flag:
                    line_ans += line[i]
                i += 1
            if len(line_ans) > 0 and not block_flag:
                ans.append(line_ans)
                line_ans = ""
        return ans
                
            
        

                
                        
                        
        