# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        ss = set(to_delete)
        if not root:
            return []
        ans = []
        roo = root.val
        def dfs(root, par,d):
            

            if not root:
                return 
            dfs(root.left, root, "l")
            dfs(root.right, root, "r")
            # print(root.val, "shsh")
            if root.val in ss:
                if d == 'l':
                    par.left = None
                else:
                    par.right = None
            elif par.val in ss or (root and root.val == roo):
                ans.append(root)
        dfs(root, root, "l")
        return ans


        