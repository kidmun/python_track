class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        parent = {}
        rank = [1] * n
        connected = {i:set([i]) for i in range(n)}
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
                    connected[parent_x].update(connected[parent_y])
                else:
                    rank[parent_y] += rank[parent_x]
                    parent[parent_x] = parent[parent_y]
                    connected[parent_y].update(connected[parent_x])
        rest = defaultdict(set)
        for a, b in restrictions:
            rest[a].add(b)
            rest[b].add(a)
        i = 0
        ans = []
        
        for a, b in requests:
            flag = True
            par_a = find(a)
            par_b = find(b)
            for x, y in restrictions:
                if (x in connected[par_a] and y in connected[par_b]) or (y in connected[par_a] and x in connected[par_b]):
                    flag = False
                    break
            if flag:
                union(a, b)
            ans.append(flag)
        return ans