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
    n  =get_int()
    graph = defaultdict(list)
    for i in range(n):
        nums = li()
        for j in range(1, len(nums) + 1):
            if nums[j - 1] == 1:
                graph[i + 1].append(str(j))
    for key in graph:
        print(len(graph[key]), *graph[key])
            
 
    
if __name__ == "__main__":
    for _ in range(1):
        solve()
