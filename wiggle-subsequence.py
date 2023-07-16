class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = [0] * n
        down = [0] * n
        up[0] = 1
        down[0] = 1
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i - 1] > nums[i]:
                up[i] = up[i - 1]
                down[i] = up[i - 1] + 1
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]
        return max(down[-1], up[-1])