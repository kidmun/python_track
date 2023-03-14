# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        def verticalTrav(root, row, col):
            if not root:
                return 
            if col in count:
                if row in count[col]:
                    insort_left(count[col][row],root.val)
                else:
                    count[col][row] = [root.val]
            else:
                count[col] = {row:[root.val]}
           
            verticalTrav(root.left, row +1, col - 1)
            verticalTrav(root.right, row+ 1,col + 1)
            return 
        count = {}
        verticalTrav(root, 0, 0)
    
        cols = sorted(count)
        ans = []
        
        for col in cols:
            res = []
            rows = sorted(count[col])
            for row in rows:
                res.extend(count[col][row])
            ans.append(res)
        return ans