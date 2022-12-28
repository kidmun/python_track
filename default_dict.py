# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
first = input().split()
n = int(first[0])
m = int(first[1])
a = []
b = []
for i in range(n):
    a.append(input())
for i in range(m):
    b.append(input())

d = defaultdict(list)
for i,w in enumerate(a):
    d[w].append(str(i+1))
for w in b:
    if len(d[w]) > 0:
        print(" ".join(d[w]))
    else:
        print(-1)
        

# for c in b:
#     ans = ""
#     for i in range(len(a)):
#         if c == a[i]:
#             ans += str(i + 1)
#             ans += " "
#     if len(ans) > 0:
#             print(ans)
#     else:
#         print(-1)
            
            
    
    