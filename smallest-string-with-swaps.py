class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = {}
        rank = [1] * len(s)
        for i in range(len(s)):
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
        for a, b in pairs:
            union(a, b)
        graph = defaultdict(list)
        for i in range(len(s)):
            graph[find(i)].append(i)
        ans = [0] * len(s)
       
        for key, li in graph.items():
            chars = []
            for val in li:
                chars.append(s[val])
            chars.sort()
            for i, ind in enumerate(li):
                ans[ind] = chars[i]
        return "".join(ans)