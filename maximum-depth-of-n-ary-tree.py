"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        ans = 0
        if not root:
            return 0
        def dfs(root, cur):
            nonlocal ans
            if not root.children:
                ans = max(cur, ans)
                return
            for r in root.children:
                dfs(r, cur + 1)
        dfs(root, 1)
        return ans