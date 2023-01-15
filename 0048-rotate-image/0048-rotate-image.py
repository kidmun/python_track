from math import ceil
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        times = ceil(len(matrix) / 2)
        count = 0
        left_top = 0
        right_top = n - 1
        right_bottom = n * n - 1
        left_bottom = right_bottom - (right_top - left_top)
        
      
        


        while (left_top != right_top != left_bottom != right_bottom) and count < ceil(n / 2):
            p1 = left_top
            p2 = right_top
            p3 = right_bottom
            p4 = left_bottom
            for i in range(p2 - p1):
                
                temp1 = matrix[left_top // n][left_top % n]
                temp2 = matrix[right_bottom // n][right_bottom % n]
                matrix[left_top // n][left_top % n] = matrix[left_bottom  // n][left_bottom  % n]
                matrix[right_bottom // n][right_bottom % n] = matrix[right_top // n][right_top % n]
                matrix[left_bottom  // n][left_bottom  % n] = temp2
                matrix[right_top // n][right_top % n] = temp1
                left_top += 1
                right_top += n
                right_bottom -= 1
                left_bottom -= n
            
            left_top = p1 + (n + 1)
            right_top = p2 +  (n - 1)
            left_bottom = p4 - (n - 1)
            right_bottom = p3 - (n + 1)
            
            count += 1



