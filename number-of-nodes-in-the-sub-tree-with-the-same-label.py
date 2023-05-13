class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for ed in edges:
            graph[ed[0]].append(ed[1])
            graph[ed[1]].append(ed[0])
        ans = [1] * n
        
        def dfs(node, par):
            nodeCount = [0] * 26
            nodeCount[ord(labels[node]) - 97] = 1
            for ne in graph[node]:
                if ne == par:
                    continue
                childCount = dfs(ne, node)
                for i in range(26):
                    nodeCount[i] += childCount[i]
            ans[node] = nodeCount[ord(labels[node]) - 97]
            return nodeCount
        dfs(0, -1)
        return ans