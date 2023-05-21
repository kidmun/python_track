class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        parent = {}
        n = len(points)
        rank = [1] * n
        for i in range(n):
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
        cost = 0
        all_path = []
        for i, p in enumerate(points):
            for j in range(n):
                if i != j:
                    all_path.append((distance(p, points[j]), i, j))
        all_path.sort()
        for d, i, j in all_path:
            if find(i) != find(j):
                union(i, j)
                cost += d
        
        return cost