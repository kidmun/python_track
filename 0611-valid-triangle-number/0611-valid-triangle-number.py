class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(2, n):
            left = 0 
            right = i - 1
            while left < right:
                if (nums[left] + nums[right]) > nums[i]:
                    res += (right - left)
                    right -= 1
                else:
                    left += 1

                    
        return res
            
        