class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        def dfs(ind, path):
            if ind == n -1:
                res.append(path[::])
            for node in graph[ind]:
                path.append(node)
                dfs(node, path)
                path.pop()
        dfs(0, [0])
        
        return res