"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        ans = 0
        graph = {}
        for e in employees:
            graph[e.id] = (e.importance, e.subordinates)

        def dfs(id):
            nonlocal ans
            ans += graph[id][0]
            for i in graph[id][1]:
                dfs(i)
        dfs(id)
        return ans