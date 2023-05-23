class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = {}
        n = len(source)
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
        for a, b in allowedSwaps:
            union(a, b)
        cont = defaultdict(dict)
        for i in range(n):
            if source[i] in cont[find(i)]:
                cont[find(i)][source[i]] += 1
            else:
                cont[find(i)][source[i]] = 1

        ans = 0
        for i, val in enumerate(target):
            if val in cont[find(i)] and cont[find(i)][val] > 0:
                cont[find(i)][val] -= 1
            else:
                ans += 1
        return ans