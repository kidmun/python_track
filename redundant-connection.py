class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        n = len(edges)
        rank = [1] * (n + 1)
        for i in range(1, n + 1):
            parent[i] = i 
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            parent_x = find(x)
            parent_y = find(y)
            if parent_x != parent_y:
                if rank[parent_x] >= rank[parent_y]:
                    rank[parent_x] += rank[parent_y]
                    parent[parent_y] = parent[parent_x]
                else:
                    rank[parent_y] += rank[parent_x]
                    parent[parent_x] = parent[parent_y]
            else:
                return [x, y]
        for a, b in edges:
            ans = union(a, b)
            if ans:
                return ans