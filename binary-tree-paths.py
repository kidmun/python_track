# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
     
        def backtrack(root, track):
          
            if not root.left and not root.right:
                track.append(str(root.val))
                res.add("->".join(track[::]))
                return 
          
            track.append(str(root.val))
            if root.left:
                backtrack(root.left, track)
                track.pop()
            if root.right:
                backtrack(root.right, track)
                track.pop()
        res = set()
        backtrack(root, [])
        return list(res)