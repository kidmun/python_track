class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans = []
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if count < k:
                    heappush(ans, -matrix[i][j])
                else:
                    heappushpop(ans, -matrix[i][j])
                count += 1
        return ans[0] * -1