class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        indegree = [0] * len(graph) 
        my_graph = defaultdict(list)
        for i, g in enumerate(graph):
            indegree[i] = len(g)
            for num in g:
                my_graph[num].append(i)
            
        
        queue = deque([])
        ans = []
        for ind in range(len(indegree)):
            if indegree[ind] == 0:
                queue.append(ind)
                ans.append(ind)
        
        while queue:
            length = len(queue)
            for _ in range(length):
                cur = queue.popleft()
                for ne in my_graph[cur]:
                    indegree[ne] -= 1
                    if indegree[ne] == 0:
                        ans.append(ne)
                        queue.append(ne)
        ans.sort()
        return ans