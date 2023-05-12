class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ss = set([])
        indegree = [0] * n
        for ed in edges:
            graph[ed[0]].append(ed[1])
            indegree[ed[1]] += 1
            ss.add(ed[1])
        queue = deque([])
        ans = [set() for _ in range(n)]
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            length = len(queue)
            for _ in range(length):
                cur = queue.popleft()
                for ne in graph[cur]:
                    indegree[ne] -= 1
                    ans[ne].add(cur)
                    for num in ans[cur]:
                        ans[ne].add(num)
                    if indegree[ne] == 0:
                        queue.append(ne)
        for i in range(n):
            ans[i] = sorted(list(ans[i]))
        return ans