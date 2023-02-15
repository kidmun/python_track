class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zeros = 0
        left = 0
        ans = 0
        for i, num in enumerate(nums):
            if num == 0:
                zeros += 1
            if zeros == 2:
                val = i - left -1
            else:
                val = i -left
            ans = max(ans, val)
            while zeros > 1 and left < i:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
                    
        return ans
                    
            
                
                    

        