class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        ans = []
        
        for quer in queries:
            flag = False
            stack = [quer[0]]
            visited = set([quer[0]])
            while stack:
                cur = stack.pop()
                if cur == quer[1]:
                    flag = True
                    break
                for ne in graph[cur]:
                    if ne not in visited:
                        stack.append(ne)
                        visited.add(ne)
            ans.append(flag)
        return ans