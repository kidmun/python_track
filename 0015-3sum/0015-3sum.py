class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        prev = None
        ans = []
        for i in range(len(nums) - 2):
            r_prev = None
            l_prev = None
            if prev != nums[i]:
                prev = nums[i]
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    if (nums[i] + nums[left] + nums[right]) < 0:
                        left += 1
                    elif (nums[i] + nums[left] + nums[right]) > 0:
                        right -= 1
                    else:
                        if nums[left] != l_prev or nums[right] != r_prev:
                            ans.append([nums[i], nums[left], nums[right]])
                            l_prev = nums[left]
                            r_prev = nums[right]
                        right -= 1
        return ans
            
        