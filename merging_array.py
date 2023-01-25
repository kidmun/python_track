n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
ans = []
p1 = 0
p2 = 0
while p1 < n and p2 < m:
    if arr1[p1] < arr2[p2]:
        ans.append(arr1[p1])
        p1 += 1
    elif arr1[p1] > arr2[p2]:
        ans.append(arr2[p2])
        p2 += 1
    else:
        ans.append(arr1[p1])
        ans.append(arr1[p1])
        p1 += 1
        p2 += 1
        
while p1 < n:
    ans.append(arr1[p1])
    p1 += 1
while p2 < m:
    ans.append(arr2[p2])
    p2 += 1
print(*ans)