class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = [] 
        dest = set([])
        for e in edges:
            dest.add(e[1])
        for i in range(n):
            if i not in dest:
                ans.append(i)
        return ans