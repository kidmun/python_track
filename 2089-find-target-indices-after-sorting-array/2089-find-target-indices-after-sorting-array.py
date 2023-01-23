class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
#         nums.sort()
#         ans = []
#         for i, num in enumerate(nums):
#             if num == target:
#                 ans.append(i)
                
#         return ans 
        large = max(nums) + 1
        count = [0] * large
        for n in nums:
            count[n] += 1
            
        counter = 0
        for index, c in enumerate(count):
            i = c
            while i > 0:
                nums[counter] = index
                counter += 1
                i -= 1
        ans = []
        for i, n in enumerate(nums):
            if n == target:
                ans.append(i)
        return ans
            
            
        
        
        
        