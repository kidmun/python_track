class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix[0])
        total = len(matrix[0]) * len(matrix)
        l_t  = 1
        r_t = len(matrix[0])
        
        r_b = len(matrix[0]) * len(matrix)
        l_b = r_b - (r_t - l_t)
        ans = []
        while l_t <= r_t and len(ans) < total:
            i = l_t
            while i < r_t and len(ans) < total:
                
                ans.append(matrix[(i - 1) // n][(i - 1) % n])
                i += 1
            while i < r_b and len(ans) < total:
               
                ans.append(matrix[(i - 1) // n][(i - 1) % n])
                
                i += n
               
                
                
            while i > l_b and len(ans) < total:
                print(l_b, i)
                ans.append(matrix[(i - 1) // n][(i - 1) % n])
                i -= 1
                
                
            while i > l_t and len(ans) < total:
               
                ans.append(matrix[(i - 1) // n][(i - 1) % n])
                i -= n
            if l_t == r_t == l_b == r_b:
                ans.append(matrix[(l_t - 1) // n][(l_t - 1) % n])
                
                break
            l_t += n + 1
            r_t += n - 1
            l_b -= n - 1
            r_b -= n + 1
            
        return ans