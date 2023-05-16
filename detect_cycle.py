from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        indegree = [0] * V
        def dfs(cur, par):
            if indegree[cur] == 2:
                return False
            if indegree[cur] == 1:
                return True
            indegree[cur] = 1
            for ne in adj[cur]:
                if ne != par:
                    if dfs(ne, cur):
                        return True
            indegree[cur] = 2
            return False
        for i in range(V):
            if indegree[i] == 0:
                if dfs(i, -1):
                    return True
        return False
