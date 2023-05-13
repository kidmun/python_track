from collections import defaultdict
input()
n = int(input())
count = defaultdict(list)
for i in range(n):
    line = list(map(int, input().split()))

    if line[0] == 1:
        a, b = line[1], line[2]
        count[a].append(b)
        count[b].append(a)
   
    elif line[0] == 2:
        if line[1] in count:
            new = count[line[1]][::]
            new = [str(x) for x in new]
            print(*new)
