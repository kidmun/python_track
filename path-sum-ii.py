# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        stack = [(root, 0, [])]
        while stack:
            cur = stack.pop()
            cur[2].append(cur[0].val)
            if cur[0].left:
                stack.append((cur[0].left, cur[1] + cur[0].val, cur[2][::]))
            if cur[0].right:
                stack.append((cur[0].right, cur[1] + cur[0].val, cur[2][::]))
            if not cur[0].left and not cur[0].right:
                if cur[1] + cur[0].val == targetSum:
                    ans.append(cur[2][::])
        return ans