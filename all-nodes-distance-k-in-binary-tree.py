# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = defaultdict(list)
        def trav(root):
            if not root.left and not root.right:
                return
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                trav(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                trav(root.right)
        trav(root)
        queue = deque([target.val])
        count = 0
        visited = set([target.val])
        while queue and count < k:
            length = len(queue)
          
            for _ in range(length):
                cur = queue.popleft()
                for ne in graph[cur]:
                    if ne not in visited:
                        visited.add(ne)
                        queue.append(ne)
            count += 1
        ans = []
        while queue:
            ans.append(queue.popleft())
        return ans