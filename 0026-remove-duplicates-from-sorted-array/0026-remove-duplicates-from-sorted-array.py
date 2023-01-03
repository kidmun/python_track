class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] != "_":
                if nums[i] == prev:
                    nums.pop(i)
                    nums.append("_")
                else:
                    prev = nums[i]
                    i += 1
            else:
                break
        return i
                
                
            
            
        