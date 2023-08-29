class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        indegree = [0] * n
        graph = defaultdict(list)
        x = m
        
        for i in range(len(group)):
            if group[i] == -1:
                group[i] = x
                x += 1
        group_graph = defaultdict(list)
        group_indegree = [0] * x
        for i, b in enumerate(beforeItems):
            indegree[i] += len(b)
            for el in b:
                graph[el].append(i)
                if group[el] != group[i]:
                    group_graph[group[el]].append(group[i])
                    group_indegree[group[i]] += 1
        def bfs(indegree, graph):
            queue = deque([])
            res = []
            for i in range(len(indegree)):
                if indegree[i] == 0:
                    queue.append(i) 
            while queue:
                x = len(queue)
                for _ in range(x):
                    cur = queue.popleft()
                    res.append(cur)
                    for ne in graph[cur]:
                        indegree[ne] -= 1
                        if indegree[ne] < 1:
                            queue.append(ne)
            return res

        items = (bfs(indegree, graph))
        groups = (bfs(group_indegree, group_graph))

        
        if len(items) != n or len(groups) != x:
            return []
        ans = defaultdict(list)
        res = []
        for i in range(n):
            ans[group[items[i]]].append(items[i])
        for i in range(x):
            res += ans[groups[i]]
        return res