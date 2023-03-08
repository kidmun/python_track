# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def greater(root, val):
            if not root:
                return 0
            left = right = 0
            if root.right:       
                right = greater(root.right,val)
         
            if right > 0: 
                root.val = root.val + right
            else:
                root.val = root.val + right + val
            if root.left:
                left = greater(root.left, root.val)
            return max(root.val, left)
        greater(root, 0)
        return root