# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def bst(left, right):     
            if left > right:
                return None    
            if left == right:
                return TreeNode(preorder[left])      
            ind = bisect_right(preorder[left+1:right+1], preorder[left])
            ind += (left + 1)
            return TreeNode(preorder[left],  bst(left + 1,ind - 1),bst(ind,right)) 
        n = len(preorder)
        ans = bst(0,n - 1)
        return ans
      

