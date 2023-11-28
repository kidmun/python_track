class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1 and nums[0] < 0:
            return nums[0]
        neg = []
        nums.sort()
        ans = 1
        zero = False
        pos = False
        for num in nums:
            if num < 0:
                neg.append(num)
            elif num > 0:
                pos =True
                ans *= num
            else:
                zero = True
        start  =1 if len(neg) %  2 else 0
        if not pos and zero and len(neg) < 2:
            return 0
        for i in range(len(neg) - start):
            ans *= (-neg[i])
        
        return ans
        