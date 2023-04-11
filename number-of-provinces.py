class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and i != j: 
                    graph[i].append(j)
        for i in range(n):
            if i not in graph:
                graph[i] = []
        def dfs(city, visited):
            if city in visited:
                return
            visited.add(city)
            for c in graph[city]:
                dfs(c, visited)
            return visited
        
        group = set([])
        count = 0
     
        for i in range(n):
            if i not in group:
                count += 1
                v = list(dfs(i, set([])))
                for city in v:
                    group.add(city)
        return count