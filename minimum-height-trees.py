class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        indegree = [0] * n
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            indegree[a] += 1
            indegree[b] += 1
        queue = deque([])
        for i, ind in enumerate(indegree):
            if ind == 1:
                queue.append((i,0))
        ans = [0] * n
        prev1, prev2 = None, None
        while queue:
            prev1 = queue[0][0]
            if len(queue) > 1:
                prev2 = queue[1][0]
            else:
                prev2 = None
            length = len(queue)
            for _ in range(length):
                cur = queue.popleft()
                for ne in graph[cur[0]]:
                    indegree[ne] -= 1
                    ans[ne] = max(ans[ne], cur[1] + 1)
                    if indegree[ne] == 1:
                        queue.append((ne, ans[ne]))
        ans = []
        if prev1 != None:
            ans.append(prev1)
        if prev2 != None:
            ans.append(prev2)
        return ans