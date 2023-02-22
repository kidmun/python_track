class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur = sum(nums[0:k])/k
        left = 1
        right = k 
        ans = cur
        cur -= (nums[0] / k)
        
        while right < len(nums):  
            cur += (nums[right] / k)
            ans = max(ans, cur)
            cur -=  (nums[left] / k)
            left += 1
            right += 1
            
        return ans
            