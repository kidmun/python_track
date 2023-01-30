class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        minimum = k
        res = nums[k]
        left = k - 1
        right = k + 1
        count = 1
        while left > -1 and right < n:
            if nums[left] >= nums[right]:
                if nums[left] < nums[minimum]:
                    val = (count + 1) * nums[left]
                    minimum = left
                    res = max(res, val)      
                else:
                    res = max(res, nums[minimum] * (count + 1))
                
                left -= 1
            else:
                if nums[right] < nums[minimum]:
                    val = (count + 1) * nums[right]
                    minimum = right
                    res = max(res, val)      
                else:
                    res = max(res, nums[minimum] * (count + 1))
                
                right += 1
            count += 1
        while left > -1:
        
            if nums[left] < nums[minimum]:
                val = (count + 1) * nums[left]
                minimum = left
                res = max(res, val)      
            else:
                res = max(res, nums[minimum] * (count + 1))

            left -= 1
            count += 1
        while right < n:
           
            if nums[right] < nums[minimum]:
                    val = (count + 1) * nums[right]
                    minimum = right
                    res = max(res, val)
                    
            else:
                res = max(res, nums[minimum] * (count + 1))

            right += 1
            count += 1

        return res  