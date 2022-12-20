# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

count = {}

begin = 0

for word in sys.stdin:
    w = word.rstrip()
    if begin != 0:
        
        if w in count:
            count[w] +=  1
        else:
            count[w] = 1
            
        
    begin += 1
ans = ""

for word in count:
    ans += str(count[word])
    ans += " "
print(len(count))
print(ans)
        