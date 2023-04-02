import sys
import math
import bisect
import heapq
import itertools
from itertools import accumulate
from sys import stdin,stdout
from math import gcd,floor,sqrt,log, ceil
from collections import defaultdict, Counter, deque
from bisect import bisect_left,bisect_right, insort_left, insort_right
    
mod=1000000007
    
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_list_strings(): return list(map(str, sys.stdin.readline().strip().split()))
    
    
def solve():
    a, b = get_ints()
    cur = a
    def gcdM(num1, num2):
        if num1 % num2 == 0:
            return num1
        return gcd(num2, num1 % num2 )
    for i in range(a + 1, b + 1):
        cur = gcdM(cur, i)
        if cur == 1:
            break
    print(cur)
if __name__ == "__main__":
    solve()
