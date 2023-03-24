# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        pref = [0]
        pref.extend(list(accumulate(preorder)))
        def bst(left, right):     
            if left > right:
                return None 
        
            if left == right:
                return TreeNode(preorder[left])
            
            ind = bisect_right(preorder[left+1:right+1], preorder[left])
            ind += (left + 1)
            ans = TreeNode(preorder[left],  bst(left + 1,ind - 1),bst(ind,right))
            
            return ans
        # preorder.sort()
        # def bst(mid, left, right):
        #     print(preorder[mid], left, right)
        #     if left >= mid or right <= mid:
        #         return TreeNode(preorder[mid])
        #     mid1 = (left + mid) // 2 
        #     mid2 = (mid + 1 + right) // 2
        #     return TreeNode(preorder[mid], bst(mid1, left, mid - 1),bst(mid2, mid + 1,right))
        n = len(preorder)
        ans = bst(0,n - 1)
        print(ans)
        return ans