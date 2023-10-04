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
    n, m, k  = ints()
    x = li()
    lad = []
    dic = defaultdict(list)
    dic[1].append((1, 1, 1, 0))
    dic[n].append((m, n, m, 0))
    dp = {}
    for i in range(k):
        a, b, c, d, h = ints()
        dp[(a, b)] = float("inf")
        dp[(c, d)] = float("inf")
        dic[a].append((b, c, d, h))
        dic[c].append((d, c, d, 0))
        lad.append((a, b, c, d, h))
    
   
    dp[(1, 1)] = 0
    for i in range(1, n + 1):
        cur = sorted(dic[i])
        
    
        for j in range(1, len(cur)):
            if (i, cur[j][0]) not in dp:
                dp[(i, cur[j][0])] = float("inf")
            dp[(i, cur[j][0])] = min(dp[(i, cur[j][0])], dp[(i, cur[j - 1][0])] + (cur[j][0] - cur[j - 1][0]) * x[i - 1])
        for j in range(len(cur) - 2, -1, -1):
            # print(cur[j], "sssgsv")
            if (i, cur[j][0]) not in dp:
                dp[(i, cur[j][0])] = float("inf")
            
            dp[(i,cur[j][0])] = min(dp[(i, cur[j][0])], dp[(i, cur[j + 1][0])] + (cur[j + 1][0] - cur[j][0]) * x[i - 1])
        for j in range(len(cur)):
            if (cur[j][1], cur[j][2]) not in dp:
                dp[(i, cur[j][0])] = float("inf")
            
            dp[(cur[j][1], cur[j][2])] = min(dp[(cur[j][1], cur[j][2])], dp[(i, cur[j][0])] - cur[j][3])
            
    return dp[(n, m)] if dp[(n, m)] != float('inf') else "NO ESCAPE"
    
if __name__ == "__main__":
    for _ in range(get_int()):
        print(solve())
