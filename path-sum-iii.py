# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        def path(root, parent, cur):
            nonlocal count
            if not root:
                return      
            val = root.val + cur
            count += parent[val-targetSum]
            parent[val] += 1
            path(root.left, parent, val)
            path(root.right, parent, val)
            parent[val] -= 1
            return 
        c = Counter()
        c[0] = 1
        path(root, c, 0)
 
        return count