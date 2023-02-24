class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 1
        left = 0
        right = 1
        inc = None
        dec = None
        while right < n:
         
            if arr[right] == arr[right - 1]:
                ans = max(ans, right - left)
                inc = dec = None
                left = right 
                
            elif arr[right] < arr[right - 1]:
                if dec:
                    ans = max(ans, right - left)
                    left = right -1
                    inc = None
                else:
                    inc = None
                    dec = True
            else:
                if inc:
                    ans = max(ans, right - left)
                    left = right - 1
                    dec = None
                else:
                    dec = None
                    inc = True
            right += 1
        ans = max(ans, right - left)
            
        return ans
            
            
            
        
       
                    

                
                
         
                
        
      
        
        