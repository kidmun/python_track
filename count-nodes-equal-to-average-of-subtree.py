# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        def average(root):
            if not root.left and not root.right:
                return [root.val, 1, 1]
            left = right = [0, 0, 0]
            if root.left:
                left = average(root.left)
            if root.right:
                right = average(root.right)
            value = left[0] + right[0] + root.val 
            value2 = 1 + left[2] + right[2]
            if root.val == (value // value2):
                return [value, left[1] + right[1] + 1, value2]
            return [value, left[1] + right[1], value2]
        return average(root)[1]