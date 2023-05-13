# author 
# Kidus Guade

import sys
from sys import stdin,stdout
from math import gcd,floor,sqrt,log, ceil,lcm
from collections import defaultdict, Counter, deque
from bisect import bisect_left,bisect_right, insort_left, insort_right
def ints(): return map(int, sys.stdin.readline().strip().split())
def li(): return list(map(int, sys.stdin.readline().strip().split()))
def string(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def li_strings(): return list(map(str, sys.stdin.readline().strip().split()))
    
def solve():
    n = get_int()
    graph =  defaultdict(list)
    sources = []
    sinks = []
    ss = set([])
    for i in range(n):
        nums = li()
        for j, num in enumerate(nums):
            if num == 1:
                graph[i + 1].append(j + 1)
                ss.add(j + 1)
    for i in range(1, n + 1):
        if i not in ss:
            sources.append(i)
        if i not in graph:
    
            sinks.append(i)
    sinks.sort()
    sources.sort()
    s = [str(len(sources))]
    for so in sources:
        s.append(str(so))
    y = [str(len(sinks))]
    for so in sinks:
        y.append(str(so))

  
    print(*s)
    print(*y)

   

    
if __name__ == "__main__":
    for _ in range(1):
        solve()
