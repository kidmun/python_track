class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def solve(n):
            if n == 0:
                return []
            if n == 1:
                return [[1]]
            prev = solve(n - 1)
            new = [1]
          
            for i in range(1, n - 1):
                new.append(prev[-1][i - 1] + prev[-1][i])
            new.append(1)
            prev.append(new)
            return prev
        return solve(numRows)

        