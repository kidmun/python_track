class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        med, sm  = float("inf"), float("inf")
        for i, num in enumerate(nums):
            if sm < med < num:
                return True
            elif num < sm:
                sm = num
            elif sm < num < med:
                med = num
        return False