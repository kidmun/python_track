class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = None
        left = 0
        right = 0
        total = 0
        while right < len(nums): 
            if total >= target:
                total -= nums[left]
                if not ans:
                    ans = right - left
                else:
                    ans = min(ans, right - left)
                left += 1
            else:
                total += nums[right]
                right += 1
                
        while total >= target and left < len(nums):
            if not ans:
                    ans = right - left
            else:
                ans = min(ans, right - left)
            total -= nums[left]
            left += 1
           
        if ans:
            return ans
        else:
            return 0
            
        
            
        