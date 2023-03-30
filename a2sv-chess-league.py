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
    n, k = get_ints()
    nums = get_list()
    def mergeSort(left, right):
        if left >= right:
            return [(left, nums[left])]
        mid = (left + right) // 2
        l_arr = mergeSort(left, mid)
        r_arr = mergeSort(mid + 1, right)
        return merge(l_arr, r_arr)
    def merge(l_arr, r_arr):
        arr = []
        p1 = 0
        p2 = 0
        
        while p1 < len(l_arr) and p2 < len(r_arr):
            if  l_arr[p1][1] < (r_arr[p2][1] - k):
                p1 += 1
            elif r_arr[p2][1] < (l_arr[p1][1] - k):
                p2 += 1
            else:
                break
        i = 0
  
        total = (len(l_arr) - p1) + (len(r_arr) - p2)
        while i < total:
            if p1 < len(l_arr) and (p2 >= len(r_arr) or l_arr[p1][1] <= r_arr[p2][1]):
                arr.append(l_arr[p1])
                p1 += 1
            else:
                arr.append(r_arr[p2])
                p2 += 1
            i += 1
        return arr
    ans = sorted(mergeSort(0, len(nums) - 1))
    res = []
    for a in ans:
        res.append(a[0]+1)
    print(*res)
            
if __name__ == "__main__":
    solve()
