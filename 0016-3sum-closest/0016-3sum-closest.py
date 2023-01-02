class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                
                res = nums[i] + nums[left] + nums[right]
                
                if (target - res) > 0:
                    ans.append(target - res)
                    left += 1
                    
                elif (target - res) < 0:
                    ans.append(target - res)
                    right -= 1
                else:
                    return res
        sm = 0
        val = abs(ans[0])
        for i in range(len(ans)):
            if abs(ans[i]) < val:
                val = abs(ans[i])
                sm = i
        return target - ans[sm]
                

        