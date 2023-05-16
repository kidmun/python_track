from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        indegree = [0] * v
     
        def dfs(cur):
            if indegree[cur] == 2:
                return False
            if indegree[cur] == 1:
                return True
            indegree[cur] = 1
            for ne in adj[cur]:
                if ne != cur:
                    if dfs(ne):
                        return True
            indegree[cur] = 2
            return False
        for i in range(v):
            if indegree[i] == 0:
                if dfs(i):
                    return True
        return False
               
            
                
                    
        
        #Code here
