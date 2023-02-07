class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        right = 0
        left = 0
        update = 0
        prev = nums[left]
        while right < len(nums):
            if nums[right] != prev:
                nums[update] = nums[right]
                left = right
                prev = nums[left]
                right += 1
                update += 1
            else:
                if (right - left) < 2:
                    nums[update] = nums[right]
                    right += 1
                    update += 1
                else:
                    right += 1
        return update
                    
                
                


        