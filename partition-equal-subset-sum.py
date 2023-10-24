class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2:
            return False
        target = total // 2
        
        # dp = [False] * (target + 1)
        # dp[0] = True
        # for i in range(len(nums)):
        #     for j in range(target, nums[i] -1, -1):
        #         dp[j] = dp[j] or dp[j - nums[i]]
        #         if dp[target]:
        #             return True
        # # print(dp)
        # return dp[target]
        s = set([0])
        for num in nums:
            temp = set()
            for el in s:
                # if target + num == target:
                #     return True
                temp.add(el)
                temp.add(el + num)
            if target in s:
                return True
            s = temp
        return True if target in s else False