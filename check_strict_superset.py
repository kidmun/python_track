# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
n = int(input())
ans = True

for i in range(n):
    s = set(input().split())
    if len(s) >= len(A):
        ans = False
        break
    for c in s:
        if c not in A:
            ans = False
            break
print(ans)
