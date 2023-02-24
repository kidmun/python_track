class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = 0
        left = 0
        ans = 0
        right = 0
        while right < len(nums):
            num = nums[right]       
            if num % 2 != 0:
                odd += 1
            if odd == k:
                ans += 1
                right += 1
                count1 = 0
                while right < len(nums) and nums[right] % 2 == 0:
                    count1 += 1
                    right += 1
                ans += count1
               
                while left < right and odd >= k:
                          
                    if nums[left] % 2 != 0:
                        odd -= 1
                    else:
                        ans += count1
                        ans += 1
                    left += 1
            else:
                right += 1
        return ans    
                    
                    
            
          