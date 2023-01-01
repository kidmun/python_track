pos = input()
col = pos[0]
row = pos[1]

if (col == 'a' or col == 'h') and (row == '1' or row == '8'):
    print(3)
elif (col == 'a' or col == 'h') or (row == '1' or row == '8'):
    print(5)
else:
    print(8)
    T = int(input())



for i in range(T):
    ran = input().split()
    l = int(ran[0])
    r = int(ran[1])
  
    i = l
    while i < r + 1:
        j = 1
        while i * j < r + 1:
            if i * j < i + 1:
                j += 1
            else:
                print(" ".join([str(i), str(i * j)]))
                i = r + 1
                j = r + 1
        i += 1     
        
      
                
            
        # while j < r + 1: 
        #     if i != 0:
        #         if j % i == 0:
        #             print(" ".join([str(i), str(j)]))
        #             j = r + 1
        #             i = r + 1
        #     j += 1
        # i += 1
                
                
    