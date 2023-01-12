t = int(input())

for test in range(t):
    row_col = input().split()
    n, m = int(row_col[0]), int(row_col[1])
    board = []
    for r in range(n):
        board.append(input().split())
    obj1 = {}   
    obj2 = {}
    for i in range(n):
        for j in range(m):
            if i - j in obj1:
                obj1[i-j] += int(board[i][j])
            else:
                obj1[i-j] = int(board[i][j])
                
            if i + j in obj2:
                obj2[i+j] += int(board[i][j])
            else:
    
                obj2[i+j] = int(board[i][j])
    large = 0 
   
    for i in range(n):
        
        for j in range(m):
            
            score = obj1[i - j] + obj2[i + j] - int(board[i][j])
            
            large = max(large, score)
   
    print(large)            
        
                
            
  
            
        
    