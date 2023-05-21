class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = {}
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
        for x, y, d in roads:
            union(x, y)
        ans = float("inf")
        for x, y, d in roads:
            if find(1) == find(x):
                ans = min(ans, d)
        return ans