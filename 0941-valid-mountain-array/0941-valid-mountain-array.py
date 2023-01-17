class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        large = max(arr)
        lar_ind = arr.index(large)
        if len(arr) < 3 or lar_ind == 0 or lar_ind == len(arr) - 1:
            return False
    
        i = 1
        
        prev = arr[0]
        while i < lar_ind:
            if arr[i] <= prev:
                return False
            
            prev = arr[i]
            i += 1
        j = lar_ind + 1
        prev = arr[lar_ind]
        while j < len(arr):
            if arr[j] >= prev:
                return False
          
            prev = arr[j]
            j += 1
        return True
            
            
            
        
            
            
            
        
        
        