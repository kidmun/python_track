class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        index = 0
        n =len(nums)
        
        count = 0
        while index < len(nums):
            if nums[index] % 2 == 0:
                temp = nums[index]
                nums.pop(index)
                nums.insert(count, temp)
                count += 1
            index += 1
        return nums