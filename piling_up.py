# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

for i in range(int(input())):
    n = int(input())
    blocks = deque(map(int, input().split()))
    while blocks:
        maximum = None
        if blocks[-1] > blocks[0]:
            maximum = blocks.pop()
        else:
            maximum= blocks.popleft()
        if len(blocks) == 0:
            print("Yes")
            break
    
        if blocks[-1] > maximum or blocks[0] > maximum:
            print("No")
            break