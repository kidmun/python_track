n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
ans = []
right = 0
for left in range(len(arr2)):
    while right < len(arr1) and arr1[right] < arr2[left]:
        right += 1
        
            
            
    arr2[left] = right
    
print(*arr2)