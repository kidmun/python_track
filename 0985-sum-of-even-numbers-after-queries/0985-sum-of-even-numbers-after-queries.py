class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        prev_sum = 0
        ans = []
        for n in nums:
            if n % 2 == 0:
                prev_sum  += n
        for q in queries:
         
            value = q[0]
            index = q[1]
            
            if nums[index] % 2 == 0:
                even = True
            else:
                even = False
            new_value = nums[index] + value    
     
           
            if new_value % 2 == 0:
                if not even:
                    prev_sum += new_value
                else:
                    prev_sum -= nums[index] 
                    prev_sum += new_value
            else:
                if even:                    
                    prev_sum -= nums[index]
            nums[index] = new_value
            ans.append(prev_sum)
        
            
        return ans
        
                
        
                
            
        