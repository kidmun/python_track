# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalance(root):
            if not root:
                return [0, True]
            val1 = isBalance(root.left)
            val2 = isBalance(root.right)
            left=  1 + val1[0]
            right= 1 + val2[0] 
            if abs(left - right) > 1:
                return [max(left, right), False]
            return [max(left, right), (val1[1] and val2[1])]
        val = isBalance(root)
        return val[1]
    