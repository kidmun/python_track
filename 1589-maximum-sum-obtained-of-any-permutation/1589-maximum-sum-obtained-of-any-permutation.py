class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        count = Counter()
        for req in requests:   
            count[req[0]] += 1
            count[req[1] + 1] -= 1           
        
        prev = 0
        val = []
        for i in range(len(nums)):
            if i in count:
                prev += count[i]
            val.append(prev)
        nums.sort()
        val.sort()
        ans = 0
        index = len(nums) - 1
        while val[index] > 0 and index > -1:
            ans += (val[index] * nums[index])   
            index -= 1
            
        return (ans % (10**9 + 7))
        
         
            
            
            
        
        
    
            
        
        
        
        
               