from collections import Counter
line = input().split()
n, m = int(line[0]), int(line[1])

table = []
for i in range(n):
    table.append(list(input()))

rows = []
cols = []
for i in range(n):
    rows.append(Counter(table[i]))

for i in range(m):
    c = []
    for j in range(n):
        c.append(table[j][i])
    cols.append(Counter(c))
        
        
 
res = ""   
for i in range(n):
    for j in range(m):
        if (rows[i][table[i][j]]) < 2 and (cols[j][table[i][j]] < 2):
            res += table[i][j]
            
            
print(res)