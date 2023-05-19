class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}
        n = len(stones)
        rank = {}
        for i in range(n):
            parent[(stones[i][0], stones[i][1])] = (stones[i][0], stones[i][1])
            rank[(stones[i][0], stones[i][1])]  = 1
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
        for i in range(n):
            for j in range(i + 1, n):
                if (stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]):
                    union((stones[i][0], stones[i][1]), (stones[j][0], stones[j][1]))

        removed = set()
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (stones[j][0], stones[j][1]) not in removed and find((stones[i][0], stones[i][1])) == find((stones[j][0], stones[j][1])):
                    count += 1
                    removed.add((stones[j][0], stones[j][1]))
        return count