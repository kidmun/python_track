class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        count = 0
        while count < len(command): 
            if command[count] == "G":
                ans += "G"
            else:
                if command[count+1] == ")":
                    ans += "o"
                    count += 1
                    
                else:
                    count += 1
                    while command[count] != ")":
                        ans += command[count]
                        count += 1
                    
            count += 1
        return ans
                        
        