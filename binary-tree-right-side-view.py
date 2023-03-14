# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        def depthCalc(root, val):     
            if not root.left and not root.right:
                return      
            if root.left:
                if val in count:
                    count[val].append(root.left.val)
                else:
                    count[val] = [root.left.val]
                depthCalc(root.left, val + 1)
            if root.right:
                if val in count:
                    count[val].append(root.right.val)
                else:
                    count[val] = [root.right.val]
                depthCalc(root.right, val + 1) 
        count = {0:[root.val]}
        depthCalc(root,1)
        ans = []
        for key in count:
            ans.append(count[key][-1])
        return ans
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        val = self.levelOrder(root)
       
        return val