class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
#         ans = []
#         for i in range(len(nums)):
#             ans.append(nums[nums[i]])
#         return ans
        n = len(nums)
        for i in range(len(nums)):
            
            nums[i] = nums[i] + (nums[nums[i]] % n) * n
        
        for i in range(n):
            nums[i] = nums[i] // n
        return nums
            
        
       


        
        