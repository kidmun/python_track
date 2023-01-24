test = int(input())

for t in range(test):
    flag = True
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(n - 1):
        if (arr[i + 1] - arr[i]) >= 2:
            flag = False
    if flag:
        print("YES")
    else:
        print("NO")