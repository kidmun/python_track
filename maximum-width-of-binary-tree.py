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
        def depthCalc(root, val, x):     
            if not root.left and not root.right:
                return      
            if root.left:
                if val in count:
                    count[val].append((root.left.val, 2 * x))
                else:
                    count[val] = [(root.left.val, 2 * x)]
                depthCalc(root.left, val + 1, 2 * x)
            if root.right:
                if val in count:
                    count[val].append((root.right.val, 2 * x+ 1))
                else:
                    count[val] = [(root.right.val, 2 * x+ 1)]
                depthCalc(root.right, val + 1, 2 * x + 1) 
        count = {0:[root.val]}
        depthCalc(root,1, 1)
        ans = []
        for key in count:
            ans.append(count[key])
        return ans
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        val = self.levelOrder(root)
        ans = 1
        if len(val) == 1:
            return 1
        for i, level in enumerate(val):
            if i > 0:
                sm = level[0][1]
                lar = level[0][1]
                for l in level:
                    sm = min(sm, l[1])
                    lar = max(lar, l[1])
                ans = max(lar - sm + 1, ans)
        return ans