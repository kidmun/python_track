class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(float("inf"))
            ans.append(row)
        for i in range(m):
            
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                else:
                    if i > 0:
                        ans[i][j] = min(ans[i][j], ans[i - 1][j] + 1)
                    if j > 0:
                        ans[i][j] = min(ans[i][j], ans[i][j - 1] + 1)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    ans[i][j] = min(ans[i][j], ans[i + 1][j] + 1)
                if j < n - 1:
                    ans[i][j] = min(ans[i][j], ans[i][j + 1] + 1)
        return ans