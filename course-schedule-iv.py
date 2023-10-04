class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        distance = [[float("inf")] * numCourses for i in range(numCourses)]
        for a, b in  prerequisites:
            distance[a][b] = 1

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        ans = []
        for a, b in queries:
            if distance[a][b] == float("inf"):
                ans.append(False)
            else:
                ans.append(True)
        return ans