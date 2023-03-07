# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkValid(root, left, right):
            if not root:
                return True
            if left >= root.val or right <= root.val:
                return False
            return checkValid(root.left, left, root.val) and checkValid(root.right,root.val, right)
        
        return checkValid(root, float('-inf'),float('inf'))