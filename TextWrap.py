import textwrap
import math
def wrap(string, max_width):
    
    index = 0
    ans = ""
    for i in range(math.ceil(len(string) / max_width)):
        
        count = 0
        
        while (index < len(string) and count < max_width):
            ans += string[index] 
            
            count += 1
            index += 1
        ans += "\n"
    return ans
      
             
    