class Solution:
    def simplifyPath(self, path: str) -> str:
        index = 0
        n = len(path)
        stack = []
        while index < n:
            if path[index] == "/":
                index += 1
                while index < n and path[index] == "/":
                    index += 1
            elif path[index] == ".":
                val = ""
            
                while index < n and (path[index] == "." or path[index] != "/") :
                    val += path[index]
                    index += 1
              
                if len(val) == 2 and val != ".." and index >= n:
                    
                    stack.append(val)
                elif len(val) == 2:
                    if stack:
                        stack.pop()

                elif len(val) > 2:
                   
                    stack.append(val)
                        
            else:
                val = ""
                while index < n and path[index] != "/":
                    val += path[index]
                    index += 1
                stack.append(val)
     
        return "/" + "/".join(stack) 
                
                    
            
        