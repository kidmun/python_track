class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        count = {}
        for req in requests:
            if req[0] in count:
                count[req[0]] += 1
            else:
                count[req[0]] = 1
            if req[1] + 1 in count:
                count[req[1] + 1] -= 1
            else:
                count[req[1] + 1] = -1
                
        nums.sort()
        prev = 0
        val = []
        for i in range(len(nums)):
            if i in count:
                prev += count[i]
            val.append(prev)
        val.sort()
        ans = 0
        index = len(nums) - 1

        while val[index] > 0 and index > -1:
            ans += (val[index] * nums[index])
           
            index -= 1
        return (ans % (10**9 + 7))
        
         
            
            
            
        
        
    
            
        
        
        
        
               