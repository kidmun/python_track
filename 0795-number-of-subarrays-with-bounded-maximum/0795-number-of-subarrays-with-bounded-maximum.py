class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        """l = 0
        r = 0
        maxx = nums[0]
        res = 0
        n = len(nums)
        while r < n:
            if nums[r] > maxx:
                maxx = nums[r]
            if maxx < left or maxx > right:
                if (r - l) > 0:
                    val = r - l        
                    res += (val * (val + 1))//2
                l = r + 1
                if l < n:
                    maxx = nums[l]
            r += 1
         
        if maxx >= left and maxx <= right:
            if (r - l) > 0:
                val = r - l
                res += (val * (val + 1))//2
            
        return res"""
        count = 0
        answer = 0
        count2 = 0
        cot = False if nums[0] >= left else True
        for i in range(len(nums)):
            if nums[i] > right:
                answer += (count * (count + 1))/2
                count = 0
            else:
                count += 1
            if nums[i] < left:
                cot = True
                count2 += 1
            elif nums[i] >= left and cot:
                cot = False
                answer -= (count2 * (count2 + 1))/2
                count2 = 0
        answer += (count * (count + 1))/2
        answer -= (count2 * (count2 + 1))/2
        return int(answer)
        
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
   
        