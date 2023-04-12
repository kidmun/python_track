# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(root, current_sum):
            nonlocal total
            if not root.left and not root.right:
                current_sum += str(root.val)
                total += int(current_sum)
                return
            if root.left:
                dfs(root.left, current_sum + str(root.val))
            if root.right:
                dfs(root.right, current_sum + str(root.val))
            return 
        dfs(root, "")
        return total