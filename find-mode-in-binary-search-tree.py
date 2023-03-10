# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def find(root):
            if not root:
                return
            count[root.val] += 1 
            find(root.left)
            find(root.right)

        count = Counter()
        find(root)
        larg = 1
        for key, amount in count.items():
            larg = max(larg, amount)
        ans = []
        for key in count:
            if count[key] == larg:
                ans.append(key)
        return ans