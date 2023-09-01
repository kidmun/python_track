class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def bfs(indegree, graph):
            queue = deque([])
            res = []
            for i in range(1, len(indegree)):
                if indegree[i] == 0:
                    queue.append(i)
            while queue:
                length = len(queue)
                for _ in range(length):
                    cur = queue.popleft()
                    res.append(cur)
                    for ne in graph[cur]:
                        indegree[ne] -= 1
                        if indegree[ne] < 1:
                            queue.append(ne)
            return res
        n = len(rowConditions)
        m = len(colConditions)
        row_indegree = [0] * (k + 1)
        col_indegree = [0] * (k + 1)
        row_graph = defaultdict(list)
        col_graph = defaultdict(list)
        for a, b in rowConditions:
            row_indegree[b] +=1 
            row_graph[a].append(b)
        for a, b in colConditions:
            col_indegree[b] +=1 
            col_graph[a].append(b)
        row = bfs(row_indegree, row_graph)
        col = bfs(col_indegree, col_graph)
        ans = [[0] * (len(col)) for _ in range(len(row))]
        dic = {}
        if len(row) < k or len(col) < k:
            return []
        for i, r in enumerate(row):
            dic[r] = i
        for i, c in enumerate(col):
            ans[dic[c]][i] = c
        return ans