n = int(input())
score = input().split()
score = [int(x) for x in score]
 
count = 0
lar = score[0]
sm = score[0]
li = [score[0]]
for i in range(1, n):
    if score[i] < sm or score[i] > lar:
        count += 1
    li.append(score[i])
    lar = max(li)
    sm = min(li)
print(count)