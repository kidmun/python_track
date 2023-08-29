class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        indegree = [0] * n 
        ans = -1
        val = {}
        def dfs(cur, count):
            nonlocal ans
       
            if indegree[cur] == 2:
                return False
            if indegree[cur] == 1:
                print(indegree, val , cur, count,count - val[cur])
                ans = max(ans, count - val[cur])
                return True
            val[cur] = count
            indegree[cur] = 1
            if edges[cur] != -1:
                if dfs(edges[cur], count + 1):
                    indegree[cur] = 2
                    return
                    
            indegree[cur] = 2
            return False
        for i in range(n):
            dfs(i, 0)
        return ans