# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = ""
        def dfs(root):
            nonlocal ans
            if not root.left and not root.right:
                ans += str(root.val)
            if root.left:
                ans += str(root.val) + "(" 
                dfs(root.left)
                ans += ")"
            if not root.left and root.right:
                ans = ans + str(root.val) + "()"  + "("
                dfs(root.right)
                ans += ")"
            if root.left and root.right:
                ans += "("
                dfs(root.right)
                ans += ")"
            return 
        dfs(root)
        return ans