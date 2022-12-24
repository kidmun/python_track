class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        obj_s = {}
        obj_t = {}
        for char in s:
            if char in obj_s:
                obj_s[char] += 1
            else: 
                obj_s[char] = 1
        for char in t:
            if char in obj_t:
                obj_t[char] += 1
            else: 
                obj_t[char] = 1
        for char in t:
            if (char not in obj_s) or (obj_t[char] != obj_s[char]):
                return char
                                     
     
            
                
       

      
        