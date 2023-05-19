class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        n = len(accounts)
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
        for i in range(n):
            for j in range(i + 1, n):
                for em in accounts[j]:
                    if em in accounts[i][1:]:
                        union(i, j)
        added = set([])
        ans = [set()]
        count = 0
        ans = [] 
        for i in range(n):
            ss = set() 
            if i not in added:
                ans.append([accounts[i][0]])
            for j in range(i, n):
                if find(i) == find(j) and j not in added:
                    for em in accounts[j][1:]:
                        ss.add(em)
                        added.add(j)
            ans[-1].extend(sorted(ss))
        return ans