n = int(input())
pats = []
for i in range(n):
    pats.append(input())
m = len(pats[0])
ans = ""
for i in range(m):
    all = None
    diff = None
    if pats[0][i] == "?":
        ques = True
    else:
        ques = False
        all = pats[0][i]
    for j in range(1, len(pats)):
        if pats[j][i] != "?":
            ques = False
            if not all:
                all = pats[j][i]
        if all:
            if all != pats[j][i] and pats[j][i] != "?":
                diff = True
                
    if diff:
        ans += "?"
    elif ques:
        ans += "x"
    elif all:
        ans += all
print(ans)
