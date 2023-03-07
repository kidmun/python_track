# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init(self):
    #     self.count = None
    #     self.ans = None
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
   
        def smallest(root, count):

            
            if not root:
                return [0,-1]
            left, ans = smallest(root.left, count)

            if left + count + 1 == k:
                ans = root.val
            right = 0
            if ans == -1:
                right, ans = smallest(root.right, left + 1 + count)

            return[right + left + 1, ans]
        return smallest(root, 0)[1]


        #     smallest(root.left)
        #     self.count += 1
        #     if self.count == k:
        #         self.ans = root.val
        #     smallest(root.right)
        
        #     return 
        # self.count = 0
        # self.ans = None
        # smallest(root)
        
        return self.ans