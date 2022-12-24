class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        n = len(nums)
        while index < n:
            if nums[index] == val:
                nums.pop(index)
                nums.append("_")
                
            else: 
                index += 1
        k = 0
        for el in nums:
            if el != "_":
                k += 1
        return k
                
        