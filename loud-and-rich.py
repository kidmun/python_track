class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        indegree = [0] * n 
        graph = defaultdict(list)
        ans = []
        for a, b in richer:
            graph[a].append(b) 
            indegree[b] += 1
        queue = deque()
        for i, val in enumerate(indegree):
            ans.append(i)
            if val == 0:
                queue.append(i)
   
        while queue:
            length = len(queue)
            for _ in range(length):
                cur = queue.popleft()
                for ne in graph[cur]:
                    indegree[ne] -= 1
                    if quiet[cur] < quiet[ne]:
                        ans[ne] = ans[cur]
                        quiet[ne] = quiet[cur]
                    if indegree[ne] == 0:
                        queue.append(ne)
        return ans