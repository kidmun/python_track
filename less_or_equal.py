line = input().split()
n, k = int(line[0]), int(line[1])

arr = list(map(int, input().split()))
arr.sort()

if k == 0:
    if arr[0] <= 1:
        print(-1)
    else:
        print(arr[0] - 1)
else:
    
    if k == n:
        print(arr[k - 1])
    else:
        if arr[k] <= arr[k-1]:
            print(-1)
        else:
            print(arr[k-1])