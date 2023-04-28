# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        d = deque([root])
        c = deque([root.val])
        total = 0
        ans = []
        while d:
            total = 0
            n = len(d)
            for i in range(len(d)):
                node = d.popleft()    
                total += node.val

                if node.left:
                    d.append(node.left)     
                if node.right:
                    d.append(node.right)
                   
            ans.append(total / n)

        return ans