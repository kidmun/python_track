class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        ans = [-1] * n
        for i in range(n):
            while stack and stack[-1][0] < nums[i]:
                ans[stack[-1][1]] = nums[i]
                stack.pop()
            stack.append((nums[i], i))
        for i in range(n):
            while stack and stack[-1][0] < nums[i]:
                ans[stack[-1][1]] = nums[i]
                stack.pop()
            stack.append((nums[i], i))
        return ans