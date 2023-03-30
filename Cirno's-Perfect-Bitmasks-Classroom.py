import sys
from sys import stdin,stdout
from math import gcd,floor,sqrt,log, ceil,lcm
from collections import defaultdict, Counter, deque
from bisect import bisect_left,bisect_right, insort_left, insort_right
    
mod=1000000007
    
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))
def get_string(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_list_strings(): return list(map(str, sys.stdin.readline().strip().split()))
    
    
    
def solve():
    n = get_int()
    ans = ""
    zero = False
    one = False
    for i in range(int(log(n, 2))+2):
        if (n & (1<<i) and not one):
            ans = i
            one = True
        elif n & (1<<i) and one:
            return 1 << ans
    if ans == 0:
        return (1 << ans)+ 2

    return (1 << ans)+ 1

        
    
if __name__ == "__main__":
    for _ in range(get_int()):
        print(solve())
