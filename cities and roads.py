from collections import Counter
n = int(input())
ans = 0
for i in range(n):
    line = list(map(int, input().split()))
    count  = Counter(line)
    ans += count[1]
print(ans // 2)

