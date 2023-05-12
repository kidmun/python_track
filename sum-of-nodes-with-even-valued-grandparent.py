# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def sumEven(root):
            if not root.left and not root.right:
                return [0, 0]
            left = right = [0, 0]
            child = 1
            if root.left:
                child = root.left.val
                left = sumEven(root.left)
            if root.right:
                child = root.right.val
                right = sumEven(root.right)
          
            if root.left and root.right:
                child = root.left.val + root.right.val
            if root.val % 2 == 0:
                return [child,left[0] + right[0]+ left[1] + right[1]]
            return [child, left[1] + right[1]]
        
        val = sumEven(root)
        return val[1]