class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        graph = defaultdict(list)
        colors = [-1] * n
        
        for dis in dislikes:
            graph[dis[0]].append(dis[1])
            graph[dis[1]].append(dis[0])
        def dfs(node, node_color):
            colors[node - 1] = node_color
            for ne in graph[node]:
                if colors[ne - 1] == node_color:
                    return False
                if colors[ne - 1] == -1:
                    if not dfs(ne, 1 - node_color):
                        return False
            return True
        for i in range(1, n+1):
            if colors[i - 1] == -1: 
                if not dfs(i, 0):                
                    return False
        return True